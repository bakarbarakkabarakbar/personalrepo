import numpy
import math
import matplotlib.pyplot as plt

N = 256
f_ECG = 256
f_INT = 512
A = 0.1
h_MEAN = 60
h_SD = 1
f1 = 0.1
f2 = 0.25
c1 = 0.1
c2 = 0.1
LF_HF_RATIO = 0.5
HR_BEAT = 60
rr_FS = 1


#CONVERT DATA KE RADIAN

sig1 = 0.5
sig2 = 1
f1 = 2*numpy.pi*f1
f2 = 2*numpy.pi*f2
c1 = 2*numpy.pi*c1
c2 = 2*numpy.pi*c2
dt = 1 / f_ECG
rr_MEAN = 60 / HR_BEAT
rr_T = 1 / rr_FS
rr_ds = int(round(2**(numpy.ceil(numpy.math.log(N*rr_MEAN/rr_T, 2)))))


w = []
for i in range(rr_ds+1):
    w += [(i-1)*2*math.pi*dt]
RSA = 0
MAYER = 0
SUM_RSA_MAYER = []
for i in range(rr_ds+1):
    RSA = (sig1)/numpy.sqrt(2*math.pi*(c1**2))*math.exp(((w[i] - f1)/c1)**2/-2)
    MAYER = (sig2)/numpy.sqrt(2*math.pi*(c2**2))*math.exp(((w[i] - f2)/c2)**2/-2)
    SUM_RSA_MAYER.append(RSA+MAYER)

INPUT_IDFT = []
for i in range (int(rr_ds/2)):
    INPUT_IDFT.append(rr_FS/2*numpy.sqrt(SUM_RSA_MAYER[i]))

for i in range (int(rr_ds/2)):
    INPUT_IDFT.append(rr_FS/2*numpy.sqrt(SUM_RSA_MAYER[len(SUM_RSA_MAYER)-i-1]))

ph = []
for i in range (int(rr_ds)):
    ph.append(2*numpy.pi*numpy.random.normal(0,0.2))

inv_r = []
inv_i = []
for i in range(int(rr_ds)):
    if len(ph)<int(rr_ds):
        ph += [0]
    inv_r += [INPUT_IDFT[i]*numpy.cos(ph[i])]
    inv_i += [INPUT_IDFT[i]*numpy.sin(ph[i])]

def rungeKutta(t, a1, a2, b1, b2):
    k1 = ny.zeros((2,1))
    k2 = ny.zeros((2,1))
    k3 = ny.zeros((2,1))
    k4 = ny.zeros((2,1))

    tetadotdot = fungsiTetadotdot(t, teta1, teta2, tetadot1, tetadot2)
    k1[0] = dt/2*tetadotdot[0]
    k1[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt/2, teta1 + dt/2*(tetadot1 + k1[0]/2), teta2 + dt/2*(tetadot2 + k1[1]/2), tetadot1 + k1[0], tetadot2 + k1[1])
    k2[0] = dt/2*tetadotdot[0]
    k2[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt/2, teta1 + dt/2*(tetadot1 + k1[0]/2), teta2 + dt/2*(tetadot2 + k1[1]/2), tetadot1 + k2[0], tetadot2 + k2[1])
    k3[0] = dt/2*tetadotdot[0]
    k3[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt, teta1 + dt*(tetadot1 + k3[0]), teta2 + dt*(tetadot2 + k3[1]), tetadot1 + 2*k3[0], tetadot2 + 2*k3[1])
    k4[0] = dt/2*tetadotdot[0]
    k4[1] = dt/2*tetadotdot[1]

    teta1baru = teta1 + dt*(tetadot1 + ((k1[0] + k2[0] + k3[0])/3))
    teta2baru = teta2 + dt*(tetadot2 + ((k1[1] + k2[1] + k3[1])/3))

    tetadot1baru = tetadot1 + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/3
    tetadot2baru = tetadot2 + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/3

    return teta1baru, teta2baru, tetadot1baru, tetadot2baru


IDFT = numpy.zeros(int(rr_ds))
x = numpy.arange(len(IDFT))

for i in range (int(rr_ds)):
    sumIDFTreal1 = 0
    sumIDFTreal2= 0
    sumIDFTimag1 = 0
    sumIDFTimag2 = 0
    for j in range (int(rr_ds)):
        g = 2*numpy.pi*i*j/N
        sumIDFTreal1 += (inv_r[j]*numpy.cos(g))/round(rr_ds)
        sumIDFTreal2 += (inv_r[j]*numpy.sin(g))/round(rr_ds)
        sumIDFTimag1 += (inv_i[j]*numpy.cos(g))/round(rr_ds)
        sumIDFTimag2 += (inv_i[j]*numpy.sin(g))/round(rr_ds)
        IDFT[i] = (sumIDFTreal1-sumIDFTreal2+sumIDFTimag1-sumIDFTimag2)/rr_ds

plt.figure()
plt.subplot(211)
plt.plot(w, SUM_RSA_MAYER, label=" PLOT RSA MAYER")
plt.legend()

plt.subplot(212)
plt.plot(x, IDFT, label="IDFT")
plt.legend()
plt.show()
