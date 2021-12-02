from numpy import *
from math import *
import matplotlib.pyplot as plt


N = 256 #jumlah rr
fsECG = 256 #frekuensi sampling ECG
rrfs = 1 #frekuensi sampling rr
T = 1/rrfs #periode sampling rr
skala = 2 #skalapengalirandomseed

hrtbt = 60
rrmean = 60/hrtbt

sig1 = 0.5
sig2 = 1
f1 = 2*pi*0.1
f2 = 2*pi*0.25
c1 = 2*pi*0.01
c2 = 2*pi*0.01

rrds = pow(2, ceil(log(N*rrmean/T,2)))
print(rrds)
dt = 1/fsECG

w = []
for i in range(0, round(rrds)):
    w += [i*2*pi*dt] #Revisi

print(max(w))

s1 = []
s2 = []
s = []
for i in range(0, round(rrds)): #Revisi
    s1 += [(sig1)/sqrt(2*pi*(c1**2))*exp(((w[i] - f1)/c1)**2/-2)]
    s2 += [(sig2)/sqrt(2*pi*(c2**2))*exp(((w[i] - f2)/c2)**2/-2)]
    s += [s1[i]+s2[i]]

#mirroring untuk IDFT
si = []
for i in range(round(rrds/2)):
    #si += [(rrfs/2)*sqrt(s[i])]
    si += [s[i]]
for i in range(round(rrds/2), round(rrds)):
    #si += [(rrfs/2)*sqrt(s[round(rrds)-i+1])]
    si += [s[round(rrds)-i]]
#print(si)

plt.figure(1)
plt.subplots_adjust(hspace=0.89)

plt.subplot(411)
plt.plot(w,s)
plt.title('RSA MAYER')
plt.xlabel('Radian/s')
plt.ylabel('Power')
plt.subplot(412)

plt.plot(arange(len(si)),si)
plt.title('RSA MAYER')
plt.xlabel('Sequence')
plt.ylabel('Power')
#plt.show()

#mencari fase yang random
ph = []
for i in range (round(rrds)):
    ph += [2*pi*random.normal(0,0.2)]
    #ph += [0]
#print(len(ph))

#print(round(rrds)) 
inv_r = []
inv_i = []
for i in range(round(rrds)):
    if len(ph)<round(rrds):
        ph += [0]
    inv_r += [si[i]*cos(ph[i])]#Rev
    inv_i += [si[i]*sin(ph[i])]#Rev

IDFT = zeros(round(rrds))
x = arange(size(IDFT))
for i in range (round(rrds)):
    sumIDFTreal1 = 0
    sumIDFTreal2= 0
    sumIDFTimag1 = 0
    sumIDFTimag2 = 0
    for j in range (round(rrds)):
        g = 2*pi*i*j/N
        sumIDFTreal1 += (inv_r[j]*cos(g))/round(rrds)
        #sumIDFTreal2 += (inv_r[j]*sin(g))/round(rrds)
        sumIDFTreal2 += 0
        #sumIDFTimag1 += (inv_i[j]*cos(g))/round(rrds)
        sumIDFTimag1 += 0
        sumIDFTimag2 += (inv_i[j]*sin(g))/round(rrds)
        IDFT[i] = (sumIDFTreal1-sumIDFTreal2+sumIDFTimag1-sumIDFTimag2)/rrds

#x = arange(size(si))

#print(IDFT/rrds)
plt.subplot(413)
plt.plot(x, IDFT)
plt.title('IDFT')
plt.xlabel('Sequence')
plt.ylabel('Amplitudo')

for i in range (len(IDFT)):
    IDFT[i] = (IDFT[i] * skala) + 1

plt.subplot(414)
plt.plot(x, IDFT)
plt.title('Perkalian Skala')
plt.xlabel('Sequence')
plt.ylabel('Amplitudo')

plt.show()
