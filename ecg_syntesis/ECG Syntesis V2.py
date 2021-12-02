from numpy import sqrt, pi, power, ceil, log2, zeros, exp, fft, random, std, arange, arctan2, sin
import matplotlib.pyplot as plot
from math import floor

numberHeartBeat = 256  # N
samplingFrequencyECG = 256  # fECG Hz
samplingFrequencyINTERNAL = 256  # fINT Hz
amplitudeNoise = 0.5  # A mV
heartRateMean = 60  # hMEAN bpm
heartRateStandartDeviation = 1  # hSTD bpm
lowFrequency = 0.1  # f1 Hz
highFrequency = 0.25  # f2 Hz
lowFrequencyStandartDeviation = 0.01  # c1 Hz
highFrequencyStandartDeviation = 0.01  # c2 Hz
lowFrequencyHighFrequencyRatio = 0.5  # gamma
samplingFrequencyRRInterval = 1
sigma1 = lowFrequencyHighFrequencyRatio
sigma2 = 1
noiseMean = 0.01
noiseStandartDeviation = 0.01
ratioStandartDeviation = 1

# Indexing P, Q, R, A Index, T
modulationFactor = sqrt(heartRateMean / 60)
ti = [10, 5, 0, 5, 25]
tetai = zeros(5)
ai = [0.1, -30, 25, -5, 50]
bi = [0.4, 0.1, 0.1, 0.1, 1]
ti[0] = ti[0] * sqrt(modulationFactor) * pi / 180
ti[1] = ti[1] * modulationFactor * pi / 180
ti[2] = ti[2] * pi / 180
ti[3] = ti[3] * modulationFactor * pi / 180
ti[4] = ti[4] * sqrt(modulationFactor) * pi / 180
tetai[0] = -pi * sqrt(modulationFactor) / 3
tetai[1] = -pi * modulationFactor / 12
tetai[2] = 0
tetai[3] = pi * modulationFactor / 12
tetai[4] = 5 * pi * sqrt(modulationFactor) / 9
ai[4] = ai[4] * power(modulationFactor, 2.5)
bi[0] = bi[0] * modulationFactor
bi[1] = bi[1] * modulationFactor
bi[2] = bi[2] * modulationFactor
bi[3] = bi[3] * modulationFactor
bi[4] = bi[4] * modulationFactor

totalData = 4096
modulationFactor = sqrt(heartRateMean / 60)
lowFrequencyRadian = 2 * pi * lowFrequency
highFrequencyRadian = 2 * pi * highFrequency
lowFrequencyStandartDeviationRadian = 2 * pi * lowFrequencyStandartDeviation
highFrequencyStandartDeviationRadian = 2 * pi * highFrequencyStandartDeviation
rrIntervalMean = 60 / heartRateMean
rrIntervalStandartDeviation = 60 * heartRateStandartDeviation / heartRateMean ** 2
samplingPeriodRRInterval = 1 / samplingFrequencyRRInterval
periodStep = 1 / samplingFrequencyECG
randomSeedScale = 2
numberRRInterval = int(power(2, ceil(log2(numberHeartBeat * rrIntervalMean / samplingPeriodRRInterval))))
rrStep = samplingFrequencyRRInterval / numberRRInterval
xAxisSpectralCharacteristics = zeros(numberRRInterval)
yAxisSpectralCharacteristics = zeros(numberRRInterval)
samplingPeriodINTERNAL = 1 / samplingFrequencyINTERNAL

for i in range(0, numberRRInterval):
    xAxisSpectralCharacteristics[i] = i * 2 * pi * rrStep
    yAxisSpectralCharacteristics[i] = sigma1 * exp(-0.5 * power((xAxisSpectralCharacteristics[i] - lowFrequencyRadian)
                                                                / lowFrequencyStandartDeviationRadian, 2)) \
                                      / sqrt(2 * pi * power(lowFrequencyStandartDeviationRadian, 2)) \
                                      + sigma2 * exp(-0.5 * power((xAxisSpectralCharacteristics[i]
                                                                   - highFrequencyRadian)
                                                                  / highFrequencyStandartDeviationRadian, 2)) \
                                      / sqrt(2 * pi * power(highFrequencyStandartDeviationRadian, 2))

plot.plot(xAxisSpectralCharacteristics, yAxisSpectralCharacteristics)
plot.xlabel("Radian")
plot.ylabel("Amplitude")
plot.title("RSA Mayer")
plot.show()

xAxisMirroring = zeros(numberRRInterval)
yAxisMirroring = zeros(numberRRInterval)
xAxisMirroring = xAxisSpectralCharacteristics

for i in range(0, numberRRInterval):
    if i < int(numberRRInterval / 2):
        yAxisMirroring[i] = yAxisSpectralCharacteristics[i]
    else:
        yAxisMirroring[i] = yAxisSpectralCharacteristics[numberRRInterval - i]

plot.plot(xAxisMirroring, yAxisMirroring)
plot.xlabel("Radian")
plot.ylabel("Amplitude")
plot.title("RSA Mayer Mirroring")
plot.show()

xAxisRandoming = zeros(numberRRInterval)
yAxisRandoming = zeros(numberRRInterval)
xAxisRandoming = xAxisMirroring

for i in range(0, numberRRInterval):
    yAxisRandoming[i] = yAxisMirroring[i] + 2 * pi * random.random_sample() * amplitudeNoise

plot.plot(xAxisRandoming, yAxisRandoming)
plot.xlabel("Radian")
plot.ylabel("Amplitude")
plot.title("RSA Mayer Mirroring Randoming")
plot.show()

xAxisIFFT = arange(numberRRInterval)
yAxisIFFT = fft.ifft(yAxisRandoming)

plot.plot(xAxisIFFT, yAxisIFFT)
plot.xlabel("Sequence")
plot.ylabel("Amplitude")
plot.title("RSA Mayer Mirroring Randoming IFFT")
plot.show()

# IFFTStandartDeviation = std(yAxisIFFT)
# ratioStandartDeviation = rrIntervalStandartDeviation / IFFTStandartDeviation

xAxisRRMean = xAxisIFFT
yAxisRatioStandartDeviation = rrIntervalMean + yAxisIFFT * ratioStandartDeviation
yAxisRRMean = rrIntervalMean + yAxisRatioStandartDeviation

print(len(xAxisRRMean))
plot.plot(xAxisRRMean, yAxisRRMean)
plot.xlabel("Sequence")
plot.ylabel("Amplitude")
plot.title("RRMean + RRMean*StandartDeviationRatio")
plot.show()

ecgLength = numberRRInterval * samplingFrequencyINTERNAL
xAxisSamplingInternal = zeros(ecgLength)
yAxisSamplingInternal = zeros(ecgLength)

for i in range(0, numberRRInterval):
    for k in range(samplingFrequencyINTERNAL):
        if i == 255:
            yAxisSamplingInternal[i * samplingFrequencyINTERNAL + k] = (1 - (k + 1) / samplingFrequencyINTERNAL) \
                                                                       * yAxisRRMean[i] \
                                                                       + (k + 1) / samplingFrequencyINTERNAL \
                                                                       * yAxisRRMean[i]
            xAxisSamplingInternal[i * samplingFrequencyINTERNAL + k] = i * samplingFrequencyINTERNAL + k
        else:
            yAxisSamplingInternal[i * samplingFrequencyINTERNAL + k] = (1 - (k + 1) / samplingFrequencyINTERNAL) \
                                                                       * yAxisRRMean[i] \
                                                                       + (k + 1) / samplingFrequencyINTERNAL \
                                                                       * yAxisRRMean[i + 1]
            xAxisSamplingInternal[i * samplingFrequencyINTERNAL + k] = i * samplingFrequencyINTERNAL + k

print(ecgLength)
plot.plot(xAxisSamplingInternal, yAxisSamplingInternal)
plot.xlabel("Sequence")
plot.ylabel("Amplitude")
plot.title("InternalSampling")
plot.show()

yAxisInterpolation = yAxisSamplingInternal
xAxisInterpolation = xAxisSamplingInternal
angularFrequency = 2 * pi / yAxisInterpolation

# totalTimeECG = 0
# i = 0
# while i <= ecgLength:
#     try:
#         totalTimeECG = totalTimeECG + yAxisSamplingInternal[i]
#         temporary = round(totalTimeECG / samplingPeriodINTERNAL)
#         for k in range(i, temporary):
#             yAxisInterpolation[k] = yAxisSamplingInternal[i]
#         i = temporary
#     except:
#         print('a')
#         break

# plot.plot(xAxisInterpolation, yAxisInterpolation)
# plot.xlabel("Sequence")
# plot.ylabel("Amplitude")
# plot.title("InternalSampling Interpolation")
# plot.show()


def ddtAlpha(time, x0, y0, z0):
    a0 = 1.0 - sqrt(x0 ** 2 + y0 ** 2)
    return a0 * x0 - angularFrequency[floor(time / samplingPeriodINTERNAL)] * y0


def ddtBeta(time, x0, y0, z0):
    a0 = 1.0 - sqrt(x0 ** 2 + y0 ** 2)
    return a0 * y0 + angularFrequency[floor(time / samplingPeriodINTERNAL)] * x0


def ddtGama(time, x0, y0, z0):
    temporary = 0
    zBaseline = 1 * sin(2 * pi * highFrequency * ti[int(time/samplingPeriodINTERNAL%4)])
    angleBaselineRadian = arctan2(y0, x0)
    deltaAngle = (angleBaselineRadian - tetai) % (2 * pi)

    for i in range(0, 4):
        temporary = temporary - ai[i] * deltaAngle[i] * exp(-0.5 * (deltaAngle[i] ** 2) / (bi[i] ** 2)) - (z0 - zBaseline)

    return temporary


ecgLength = totalData
k1RungeKutta = zeros(3)  # X, Y, Z
k2RungeKutta = zeros(3)  # X, Y, Z
k3RungeKutta = zeros(3)  # X, Y, Z
k4RungeKutta = zeros(3)  # X, Y, Z
initialConditionRungeKutta = [0.1, 0.0, 0.04]  # X, Y, Z
resultRungeKutta = zeros((3, ecgLength))
xAxisRungeKutta = zeros(ecgLength)
timeRungeKutta = 0

for i in range(ecgLength):
    resultRungeKutta[0][i] = initialConditionRungeKutta[0]
    resultRungeKutta[1][i] = initialConditionRungeKutta[1]
    resultRungeKutta[2][i] = initialConditionRungeKutta[2]

    k1RungeKutta[0] = ddtAlpha(timeRungeKutta, initialConditionRungeKutta[0],
                               initialConditionRungeKutta[1], initialConditionRungeKutta[2])
    k1RungeKutta[1] = ddtBeta(timeRungeKutta, initialConditionRungeKutta[0],
                              initialConditionRungeKutta[1], initialConditionRungeKutta[2])
    k1RungeKutta[2] = ddtGama(timeRungeKutta, initialConditionRungeKutta[0],
                              initialConditionRungeKutta[1], initialConditionRungeKutta[2])

    k2RungeKutta[0] = ddtAlpha(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                               initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[0],
                               initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[1],
                               initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[2])
    k2RungeKutta[1] = ddtBeta(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[2])
    k2RungeKutta[2] = ddtGama(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k1RungeKutta[2])

    k3RungeKutta[0] = ddtAlpha(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                               initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[0],
                               initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[1],
                               initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[2])
    k3RungeKutta[1] = ddtBeta(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[2])
    k3RungeKutta[2] = ddtGama(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k2RungeKutta[2])

    k4RungeKutta[0] = ddtAlpha(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                               initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[0],
                               initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[1],
                               initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[2])
    k4RungeKutta[1] = ddtBeta(timeRungeKutta + samplingPeriodINTERNAL * 0.5,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * 0.5 * k3RungeKutta[2])
    k4RungeKutta[2] = ddtGama(timeRungeKutta + samplingPeriodINTERNAL,
                              initialConditionRungeKutta[0] + samplingPeriodINTERNAL * k3RungeKutta[0],
                              initialConditionRungeKutta[1] + samplingPeriodINTERNAL * k3RungeKutta[1],
                              initialConditionRungeKutta[2] + samplingPeriodINTERNAL * k3RungeKutta[2])

    initialConditionRungeKutta[0] = initialConditionRungeKutta[0] \
                                    + samplingPeriodINTERNAL / 6 * (k1RungeKutta[0] + 2 * k2RungeKutta[0]
                                                                    + 2 * k3RungeKutta[0] + k4RungeKutta[0])
    initialConditionRungeKutta[1] = initialConditionRungeKutta[1] \
                                    + samplingPeriodINTERNAL / 6 * (k1RungeKutta[1] + 2 * k2RungeKutta[1]
                                                                    + 2 * k3RungeKutta[1] + k4RungeKutta[1])
    initialConditionRungeKutta[2] = initialConditionRungeKutta[2] \
                                    + samplingPeriodINTERNAL / 6 * (k1RungeKutta[2] + 2 * k2RungeKutta[2]
                                                                    + 2 * k3RungeKutta[2] + k4RungeKutta[2])

    xAxisRungeKutta[i] = i
    timeRungeKutta = timeRungeKutta + samplingPeriodINTERNAL

plot.plot(xAxisRungeKutta, resultRungeKutta[0])
plot.plot(xAxisRungeKutta, resultRungeKutta[1])
plot.plot(xAxisRungeKutta, resultRungeKutta[2])
plot.xlabel("Sequence")
plot.ylabel("Amplitude")
plot.title("Runge Kutta")
plot.show()

xResampling = zeros(ecgLength)
yResampling = zeros(ecgLength)
zResampling = zeros(ecgLength)

i = 0
j = 0
while i <= ecgLength:
    try:
        xResampling[j] = resultRungeKutta[0][i]
        yResampling[j] = resultRungeKutta[1][i]
        zResampling[j] = resultRungeKutta[2][i]

        i = i + round(samplingFrequencyINTERNAL / samplingFrequencyECG)
        j = j + 1
    except:
        break

totalDataResampling = j
zResamplingRange = zResampling.max() - zResampling.min()
xAxisFinalECG = zeros(totalDataResampling)
yAxisFinalECG = zeros(totalDataResampling)

for i in range(totalDataResampling):
    yAxisFinalECG[i] = (zResampling[i] - zResampling.min()) * 1.6 / zResamplingRange - 0.4
    yAxisFinalECG[i] = yAxisFinalECG[i] + random.normal(noiseMean, noiseStandartDeviation)
    xAxisFinalECG[i] = i

plot.plot(xAxisFinalECG, yAxisFinalECG)
plot.xlabel("Sequence")
plot.ylabel("Amplitude")
plot.title("Final ECG")
plot.show()
