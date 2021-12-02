import numpy
from matplotlib.pylab import *
import matplotlib.animation as animation

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()
print(filename)
f = open(filename, 'r')
data = f.readlines()

for a in range(0, len(data)):
    data[a] = data[a].replace('\n', '')
    data[a] = data[a].replace(' ', '')
    data[a] = data[a].replace('(', '')
    data[a] = data[a].replace(')', '')
    data[a] = data[a].split('\t')
    if a == 0:
        str11 = data[a][0]
        str12 = data[a][1]
        str13 = data[a][2]
        continue
    if a == 1:
        sample_interval = float(data[a][0].replace('sec', ''))
        satuan_data1 = data[a][1]
        satuan_data2 = data[a][2]
        continue
    data[a][0] = int(data[a][0])
    data[a][1] = float(data[a][1])
    data[a][2] = float(data[a][2])

del data[0]
del data[0]

data = np.array(data)
data1 = data[:, 1]
data2 = data[:, 2]

periodesampling = sample_interval
frekuensisampling = 1/periodesampling
lebar_grafik = 1000


t1 = 0
t=arange(lebar_grafik)*periodesampling
yp1=zeros(lebar_grafik)
yp2=zeros(lebar_grafik)

fig = figure(num = 0, figsize = (10, 4))
fig.suptitle("ECG HEART RATE DETECTION", fontsize=12)
ax1 = subplot2grid((1, 2), (0, 0))
ax2 = subplot2grid((1, 2), (0, 1))

ax1.set_title('ECG In Time Domain')
ax2.set_title('Heart Rate Peak Detection')


ax1.set_ylim(min(data1) - 0.2, max(data1) + 0.2)
ax2.set_ylim(min(data2) - 0.2, max(data2) + 0.2)

ax1.set_xlabel("Waktu - Frekuensi Sampling " + str(int(frekuensisampling)) + "Hz")
ax2.set_xlabel("Waktu - Frekuensi Sampling " + str(int(frekuensisampling)) + "Hz")

ax1.set_ylabel("Amplitudo " + satuan_data1)
ax2.set_ylabel("Amplitudo " + satuan_data2)


ax1.set_xlim(0,lebar_grafik)
ax2.set_xlim(0,lebar_grafik)

ax1.grid(True)
ax2.grid(True)

p1, = ax1.plot(t, yp1)
p2, = ax2.plot(t, yp1)

#HANNING DEF VARIABLE
whan =[]
for n in range(0, lebar_grafik):
    whan.append(0.5 - 0.5 * numpy.cos((2 * numpy.pi * n) / (lebar_grafik - 1)))


def plotdft(data):
    e = 0
    hasil = numpy.fft.fft(data)

    # for m in range (0, jumlahdata):
    #     for n in range (0, jumlahdata):
    #         e += data[n] * numpy.exp(-2j * numpy.pi * m * n / jumlahdata)
    #     hasil.insert(m, math.sqrt(math.pow(e.real, 2)+math.pow(e.imag, 2)))
    #     e = 0

    return numpy.array(hasil)


def animasigerak(num):
    global yp1
    global yp2
    global t
    global t1

    temp = zeros(lebar_grafik)

    #if num < lebar_grafik-1:
    #    yp2[t1] = data[num]
    #else:
    #    yp2 = plotdft(lebar_grafik, yp1)

    yp1[t1] = data1[num]
    yp2[t1] = plotdft(data1)
    #yp2[t1] = data[num]*whan[t1]

    if t1 >= lebar_grafik-1:
        t1 = 0

    p1.set_data(t, yp1)
    p2.set_data(t, yp2)

    t1 += 1

    return p1, p2


line_ani = animation.FuncAnimation(fig, animasigerak, frames=len(data), interval=periodesampling, blit=True, repeat=True)

show()