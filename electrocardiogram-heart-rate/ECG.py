from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy
import math

FREQUENCY_SAMPLING = 500
PERIOD = 1/FREQUENCY_SAMPLING
INTERVAL_START = 0
INTERVAL_END = 5000
INTERVAL_LEN = INTERVAL_END - INTERVAL_START

def lpf_orde_1(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []

    periode_local = 1 / frek_sampling_local
    wc_local = 2*math.pi*fc_local

    ydata_local.insert(0, (wc_local*xdata_local[0])/((2/periode_local)+wc_local))

    for n in range(1, len(xdata_local)):
        ydata_local.insert(n, (((2/periode_local)-wc_local)*ydata_local[n-1]+wc_local*xdata_local[n]+wc_local*xdata_local[n-1])/((2/periode_local)+wc_local))

    return ydata_local

def hpf_orde_1(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []

    periode_local = 1 / frek_sampling_local
    wc_local = 2 * math.pi * fc_local

    ydata_local.insert(0, (2 * xdata_local[0]  / (2 + (wc_local * periode_local))))

    for n in range(1, len(xdata_local)):
        ydata_local.insert(n, (2 * xdata_local[n] - 2 * xdata_local[n - 1] - (wc_local * periode_local - 2) * ydata_local[n - 1]) / (2 + (wc_local * periode_local)))

    return ydata_local

def dft(data_local):
    e_local = 0
    e_local = e + 0j * e_local
    hasil_local = []
    jumlahdata_local = len(data_local)

    for k in range(0, jumlahdata_local):
        for n in range(0, jumlahdata_local):
            e_local += data_local[n] * numpy.exp(-2j * numpy.pi * k * n / jumlahdata_local)
        hasil_local.append(abs(e_local) / jumlahdata_local)
        e_local = 0 + 0j * e_local

    return hasil_local

#DATA AKUISISI

Tk().withdraw()
filename = askopenfilename()
print(filename)
f = open(filename, 'r')
data = f.readlines()

for a in range(0, len(data)):
    data[a] = float(data[a].replace('\n', ''))

ECG = numpy.array(data)
X = numpy.arange(len(ECG))

jumlahdata = INTERVAL_END - INTERVAL_START

e = 0
e = e + 0j*e

ECG = ECG[INTERVAL_START:INTERVAL_END]

#BAND PASS FILTER WITH CASCADED LPF AND HPF
hasil = hpf_orde_1(lpf_orde_1(ECG, FREQUENCY_SAMPLING, 14), FREQUENCY_SAMPLING, 10)


'''
hasil.append((2*ECG[n])/(2+(2*numpy.pi*FREQUNCY_CUTOFF*PERIOD)))


for n in range (1, jumlahdata):
    hasil.append((2*x[n]-2*x[n-1]-(wp*T-2)*y[n-1])/(2+(wp*T)))

'''
#SQUARING METHOD

for i in range(len(hasil)):
    hasil[i] = hasil[i]**2


#LOW PASS METHOD
hasil = lpf_orde_1(hasil, FREQUENCY_SAMPLING, 5)

'''
hasil1 =[]

for k in range(0, jumlahdata):
    for n in range(0, jumlahdata):
        e += hasil[n] * numpy.exp(-2j * numpy.pi * k * n / jumlahdata)
    hasil1.append(abs(e) / jumlahdata)
    e = 0 + 0j*e

for n in range(0, len(data_hr)):
    if maxvalue < data_hr[n]:
        maxvalue = data_hr[n]
        nmaxvalue = n
    if (data_hr[n] < maxvalue * 0.707) & (maxvalue > 0.02) & (status == 0):
        rvalue_array.append(maxvalue)
        r_array.append(nmaxvalue)
        maxvalue = 0
        nmaxvalue = 0
        status = 1
    if data_hr[n] < 0.02:
        status = 0
'''

#RR DETECTION

data_hr = hasil
rvalue_array = []
r_array = []
hr_array = []
maxvalue = 0
nmaxvalue = 0
status = 0

for n in range(0, len(data_hr)):
    if data_hr[n] > 0.01:
        if data_hr[n] > maxvalue:
            maxvalue = data_hr[n]
            nmaxvalue = n
            status = 1
    if data_hr[n] < 0.01:
        if status == 1:
            rvalue_array.append(maxvalue)
            r_array.append(nmaxvalue)
            status = 0
            maxvalue = 0


#CONVERT SEQUENCE TO HEART RATE

for n in range(1, len(r_array)):
    if (r_array[n] - r_array[n - 1]) / FREQUENCY_SAMPLING * 60 > 10 :
        hr_array.append((r_array[n] - r_array[n - 1]) / FREQUENCY_SAMPLING * 60)


#PLOT DATA TO GRAPH
plt.figure()
plt.plot(list(range(len(hasil))), hasil, label="Filtered QRS Komplex")
plt.ylabel('Amplitude')
plt.xlabel('Sequence')
plt.legend()


plt.figure()
plt.bar(list(range(len(hr_array))), hr_array, label="HeartRate")
plt.ylabel('Heart Rate')
plt.xlabel('Heart Beat Sequence')
plt.legend()
'''
plt.figure()
plt.plot(X[INTERVAL_START:INTERVAL_END], ECG, label="Data Input ECG")
plt.ylabel('Amplitude (mV)')
plt.xlabel('Sequence')
plt.legend()
plt.show()
plt.figure()
plt.plot(X[0:INTERVAL_LEN], dft(ECG), label="ECG DFT")
plt.ylabel('Amplitude (mV)')
plt.xlabel('Frequency')
plt.legend()

'''

plt.show()