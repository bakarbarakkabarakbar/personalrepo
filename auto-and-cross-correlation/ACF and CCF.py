import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
import ctypes

ctypes.windll.user32.MessageBoxW(0, "Select the input from the text file in the input folder!", "Auto Correlation and Cross Correlation Program", 0)

#GANTI ACF_START DAN ACF_END SEBELUM MEMULAI PROGRAM

frequency_sampling = 500
ACF_START = 0
ACF_END = 511
ACF_LEN = ACF_END - ACF_START

Tk().withdraw()
filename = askopenfilename()
print(filename)
f = open(filename, 'r')
data = f.readlines()

for a in range(0, len(data)):
    data[a] = float(data[a].replace('\n', ''))

X = np.arange(len(data))
hrstatus = 0

'''
with open('ECG.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    ECG1 = []
    ECG2 = []
    for row in csv_reader:
        if line_count == 0:
            print(row)
        else:
            ECG1.append(float(row[1]))
            ECG2.append(float(row[2]))
        line_count += 1
    print(f'Processed {line_count} lines.')


with open('Sinus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    line_count = 0
    ECG1 = []
    ECG2 = []
    for row in csv_reader:
        ECG1.append(float(float(row[0])))
        ECG2.append(float(float(row[0])))
        line_count += 1
    print(f'Processed {line_count} lines.')


ECG1 = np.array(ECG1)
ECG2 = np.array(ECG2)
X = np.arange(len(ECG1[ACF_START:ACF_END]))
#b, a = signal.butter(5, 0.5, 'low')
#output = signal.filtfilt(b, a, ECG)


def MLII():
    plt.figure()
    plt.plot(X, ECG1[ACF_START:ACF_END], label="MLII")
    plt.ylabel('Amplitude (mV)')
    plt.xlabel('Sequence')
    plt.legend()
    plt.show()
'''

def Plot_Input():
    plt.figure()
    plt.plot(X[ACF_START:ACF_END], data[ACF_START:ACF_END], label="Data Input")
    plt.ylabel('Amplitude (mV)')
    plt.xlabel('Sequence')
    plt.legend()
    plt.show()

def ACF_with_mean():
    ACF_data = np.zeros(ACF_LEN)
    temp1 = 0
    temp2 = 0

    mean = np.mean(data[ACF_START:ACF_END])
    for k in range(0, ACF_LEN):
        for i in range(ACF_START, ACF_END):
            if i + k == len(data):
                break
            temp1 = temp1 + (data[i] - mean) * (data[i + k] - mean)
            temp2 = temp2 + (data[i] - mean)**2
        ACF_data[k] = temp1/temp2
        temp1 = 0
        temp2 = 0

    plt.figure()
    plt.plot(X[0:ACF_LEN], ACF_data, label="ACF with mean")
    plt.ylabel('R')
    plt.xlabel('k')
    plt.legend()
    plt.show()

def ACF():
    ACF_data = np.zeros(ACF_LEN)

    for k in range(0, ACF_LEN):
        for l in range(ACF_START, ACF_END):
            if l + k >= len(data):
                break
            ACF_data[k] = ACF_data[k] + abs((data[k] ** 2) * np.exp(2j * np.pi * k * l / ACF_LEN))
        ACF_data[k] = abs(ACF_data[k]) / ACF_LEN

    if hrstatus == 1 :
        return ACF_data

    plt.figure()
    plt.plot(X[0:ACF_LEN], ACF_data, label="ACF")
    plt.ylabel('R')
    plt.xlabel('k')
    plt.legend()
    plt.show()

def CCF_with_noise():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
    f = open(filename, 'r')
    data2 = f.readlines()

    for a in range(0, len(data2)):
        data2[a] = float(data2[a].replace('\n', ''))

    CCF_data = np.zeros(ACF_LEN)

    noise = np.random.normal(0, 0.1, len(data))
    data_noise = data + noise

    for k in range(0, ACF_LEN):
        for l in range(ACF_START, ACF_END):
            if l + k >= len(data_noise):
                break
            CCF_data[k] = CCF_data[k] + abs((data_noise[k] * data2[k]) * np.exp(2j * np.pi * k * l / ACF_LEN))
        CCF_data[k] = CCF_data[k] / ACF_LEN

    plt.figure()
    plt.plot(X[0:ACF_LEN], CCF_data, label="CCF")
    plt.ylabel('R')
    plt.xlabel('k')
    plt.legend()
    plt.show()

def HeartRate():
    global hrstatus
    hrstatus = 1
    rrstatus = 0
    data_hr = ACF()

    #Mencari Titik RR Tertinggi
    rvalue_array = []
    r_array = []
    hr_array = []
    maxvalue = 0
    nmaxvalue = 0

    for n in range(0, len(data_hr)):
        if data_hr[n] > 0.2:
            if data_hr[n] > maxvalue:
                maxvalue = data_hr[n]
                nmaxvalue = n
                rrstatus = 1
        if data_hr[n] < 0.2:
            if rrstatus == 1 :
                rvalue_array.append(maxvalue)
                r_array.append(nmaxvalue)
                rrstatus = 0
                maxvalue = 0

    print(rvalue_array)

    for n in range(1, len(r_array)):
        hr_array.append((r_array[n] - r_array[n - 1]) / frequency_sampling * 60)

    '''
    for n in range(2, len(data_hr)):
        if (data_hr[n] > 0.3) & (data_hr[n-2] > data_hr[n-3]) & (data_hr[n-3] > data_hr[n-4]) & (data_hr[n-2] < data_hr[n-1]) & (data_hr[n-1] < data_hr[n]):
            r_array.append(n-2)
            cek.append(data_hr[n-2])

    hr_array = []
    for n in range(1, len(r_array)):
        hr_array.append((r_array[n]-r_array[n-1])/frequency_sampling*60)
    print(r_array, cek)
    '''

    hrstatus = 0
    plt.figure()
    plt.bar(X[0:len(hr_array)], hr_array, label="HeartRate")
    plt.ylabel('BPM')
    plt.xlabel('Sequence')
    plt.legend()
    plt.show()

def noise_Signal():
    data_noise = data
    amp=0.9
    noise=0.1
    for a in range (len(data_noise)):
        data_noise[a]=data_noise[a]*amp+np.random.normal(0,noise)

    plt.figure()
    plt.plot(X, data_noise)
    plt.ylabel('Amplitude')
    plt.xlabel('Sequence')
    plt.legend()
    plt.show()



windows=Tk()

b1=Button(windows, text='Plot Input Data', command=Plot_Input)
b1.pack()

# b3=Button(windows, text='Auto Correlation With Mean', command=ACF_with_mean)
# b3.pack()

l1 = Label(windows, text='Auto Correlation from the input data,')
l1.pack()

b4=Button(windows, text='ACF', command=ACF)
b4.pack()

l2 = Label(windows, text='Cross Correlation from the input data, Please select the correlation data')
l2.pack()

b5=Button(windows, text='Show Signal', command=noise_Signal)
b5.pack()

b6=Button(windows, text='CCF', command=CCF_with_noise)
b6.pack()

l2 = Label(windows, text='Find the Peak and Period from the ECG text file data,')
l2.pack()

b6=Button(windows, text='Heart Rate', command=HeartRate)
b6.pack()

windows.mainloop()