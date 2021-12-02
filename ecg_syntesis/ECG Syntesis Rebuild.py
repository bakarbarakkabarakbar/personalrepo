import numpy
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#deklarasivariableyangdigunakan
jumlahheartbeat = 256
frekuensisamplingecg = 256
frekuensisampinginternal = 512
amplitudonoise = 0.1
ratarataheartrate = 60
standartdeviasiheartrate = 1
frekuensi1 = 2*numpy.pi*0.1
sigma1kuadrat = 0.5
standartdeviasifrekuensi1 = 2*numpy.pi*0.01
frekuensi2 = 2*numpy.pi*0.25
sigma2kuadrat = 1
standartdeviasifrekuensi2 = 2*numpy.pi*0.01
rasiofrekuensi = 0.5
rasioskala = 2
dt = 1/frekuensisamplingecg
rungekuttainputx0 = 0
rungekuttaoutputy0 = 0
deltah = 1

#deklarasifungsiyangdibutuhkan
# def rungekuttaorde4(inputdatay, inputx0, inputy0, deltah):
#     limitasi = int(len(inputdatay) / deltah)  # mencaritotaliterasidaritiapstepsizedanjumlahdata
#     hasilrungekutta = numpy.zeros(len(inputdatay))
#     sequencedata = numpy.arange(len(inputdatay))
#     hasilrungekutta[0] = inputy0 #outputpertamadarirungekutta
#     inputdatax = numpy.arange(len(inputdatay)) #arraysequencedarifungsi
#     interpolasi = interp1d(inputdatax, inputdatay) #deklarasifungsiinterpolasi
#
#     for j in range(len(sequencedata)-1):
#         k1 = deltah*interpolasi(inputx0)
        # k2 = deltah*interpolasi(inputx0+0.5*deltah)
        # k3 = deltah*interpolasi(inputx0+0.5*deltah)
        # k4 = deltah*interpolasi(inputx0+deltah)
        # k1 = deltah*inputdatay[j]
        # k2 = deltah*(inputdatay[j]+inputdatay[j+1])/2
        # k3 = deltah*(inputdatay[j]+inputdatay[j+1])/2
        # k4 = deltah*inputdatay[j+1]
        # hasilrungekutta[j] = (k1+2*k2+2*k3+k4)/6
        # inputx0 += deltah #persiapaniterasiselanjutnya

    # plt.figure(5)
    # plt.plot(sequencedata, hasilrungekutta, label='ECG Signal Result')
    # plt.xlabel('Sequence')
    # plt.ylabel('Amplitudo')
    # plt.legend(loc='best')
    # plt.show()

def rungekuttaordeempat(inputdatay, inputx0, outputy, deltah):
    hasilrungekutta = []
    hasilrungekutta.append(outputy)
    temporary1 = outputy
    for j in range(1, len(inputdatay)-2, 2):
        print('a')
        k1 = deltah * inputdatay[j]
        k2 = deltah * inputdatay[j+1]
        k3 = deltah * inputdatay[j+1]
        k4 = deltah * inputdatay[j+2]
        temporary1 = temporary1+(k1+2*k2+2*k3+k4)/6
        hasilrungekutta.append(temporary1)

    plt.figure(5)
    plt.plot(numpy.arange(len(hasilrungekutta)), hasilrungekutta, label='ECG Signal Result')
    plt.xlabel('Sequence')
    plt.ylabel('Amplitudo')
    plt.legend(loc='best')
    plt.show()

frekuensi = []
for j in range(jumlahheartbeat):
    frekuensi.append(2*j*numpy.pi*dt)

#membangunsinyalrsamayerberdasarkanrumusdasar
rsamayer = []
for j in range(jumlahheartbeat):
    temporary1 = sigma1kuadrat/numpy.sqrt(2*numpy.pi*standartdeviasifrekuensi1**2)*numpy.exp((frekuensi[j]-frekuensi1)**2/standartdeviasifrekuensi1**2/-2)
    temporary2 = sigma2kuadrat/numpy.sqrt(2*numpy.pi*standartdeviasifrekuensi2**2)*numpy.exp((frekuensi[j]-frekuensi2)**2/standartdeviasifrekuensi2**2/-2)
    rsamayer.append(temporary1+temporary2)

plt.figure(0)
plt.plot(frekuensi, rsamayer, label='RSA MAYER Waves')
plt.xlabel('Omega Rad/s')
plt.ylabel('Power Spektrum')
plt.legend(loc='best')


#mirroringsinyalrsamayeruntukprosesidft
for j in range(jumlahheartbeat):
#     rsamayer[jumlahheartbeat-j-1] = rsamayer[j]
     rsamayer.append(rsamayer[jumlahheartbeat-j-1])
     frekuensi.append(2*(j+jumlahheartbeat)*numpy.pi*dt)

# plt.figure(1)
# plt.plot(frekuensi, rsamayer, label='RSA MAYER Waves Mirrorred')
# plt.xlabel('Omega Rad/s')
# plt.ylabel('Power Spektrum')
# plt.legend(loc='best')

#menambahrandomgaussianpadahasilmirrorrsamayer
for j in range(len(rsamayer)):
    rsamayer[j] += numpy.random.normal(0, 0.4)

plt.figure(2)
plt.plot(frekuensi, rsamayer, label='RSA MAYER Waves Mirrorred with Noise Gaussian')
plt.xlabel('Omega Rad/s')
plt.ylabel('Power Spektrum')
plt.legend(loc='best')

#melakukanidft
rsamayeridft = numpy.fft.ifft(rsamayer)[0:255]
sequencedata = numpy.arange(len(rsamayeridft))

plt.figure(3)
plt.plot(sequencedata, rsamayeridft, label='Result of IDFT')
plt.xlabel('Sequence')
plt.ylabel('Amplitudo')
plt.legend(loc='best')

#melakukanrasiodanskalarsertakonversiimajiner
rsamayerrasiodanskalar = []
for j in range(len(rsamayeridft)):
    #rsamayerrasiodanskalar.append(numpy.sqrt(rsamayeridft[j].real**2+rsamayeridft[j].imag**2))
    #rsamayerrasiodanskalar[j] = rsamayerrasiodanskalar[j]*rasioskala
    #rsamayerrasiodanskalar[j] += 1
    rsamayerrasiodanskalar.append(rsamayeridft[j]*rasioskala)
    rsamayerrasiodanskalar[j] += 1

plt.figure(4)
plt.plot(sequencedata, rsamayerrasiodanskalar, label='Result of IDFT After Scalar and Rasio Processing')
plt.xlabel('Sequence')
plt.ylabel('Amplitudo')
plt.legend(loc='best')

rungekuttaordeempat(rsamayerrasiodanskalar, rungekuttainputx0, rungekuttaoutputy0, deltah) #stepterakhir