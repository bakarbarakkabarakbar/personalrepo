#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from tkinter import *
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as plt
import numpy
from scipy.signal import find_peaks

jumlahdata=0
data=[]

def inputdata(): # File Box Open Window
    global jumlahdata
    global data

    Tk().withdraw()
    filename=askopenfilename()
    function=open(filename, 'r')
    data=function.readlines()

    # Turning The Raw Data to Valid Data
    for i in range(0, len(data)):
        data[i]=float(data[i].replace('\n', ''))
    jumlahdata=len(data)

    print(jumlahdata)

    plt.figure(1)
    plt.plot(numpy.arange(jumlahdata), data, label='Plot Input Data')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

def autocorrelation():
    acfoutput=numpy.zeros(jumlahdata)

    for k in range(0, jumlahdata):
        for l in range(0, jumlahdata):
            if l+k>=jumlahdata:
                break
            acfoutput[k]=acfoutput[k]+abs((data[k]**2)*numpy.exp(2j*numpy.pi*k*l/jumlahdata))
        acfoutput[k]=abs(acfoutput[k])/jumlahdata

    plt.figure(2)
    plt.plot(numpy.arange(jumlahdata), acfoutput, label='Plot Auto Correlation')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

def crosscorrelation():
    amplitudo=float(amplitudotkinter.get())
    noise=float(noisetkinter.get())
    ccfoutput=numpy.zeros(jumlahdata)
    datanoise=numpy.zeros(jumlahdata)

    for k in range(0, jumlahdata):
        for l in range(0, jumlahdata):
            if l+k>=jumlahdata:
                break
            ccfoutput[k]=ccfoutput[k]+abs((((data[k]+numpy.random.normal(0, noise))*amplitudo)*data[k])*numpy.exp(2j*numpy.pi*k*l/jumlahdata))
        datanoise[k]=data[k]+numpy.random.normal(0, noise)*amplitudo
        ccfoutput[k]=ccfoutput[k]/jumlahdata

    plt.figure(3)
    plt.plot(numpy.arange(jumlahdata), datanoise, label='Input Data after Noise Generation')
    plt.xlabel('Sequence')
    plt.ylabel('Amplitudo')
    plt.legend(loc="best")

    plt.figure(4)
    plt.plot(numpy.arange(jumlahdata), ccfoutput, label='Plot Cross Correlation')
    plt.xlabel('Sequence')
    plt.ylabel('Amplitudo')
    plt.legend(loc="best")
    plt.show()

def ecgperiod():
    acfoutput = numpy.zeros(jumlahdata)

    for k in range(0, jumlahdata):
        for l in range(0, jumlahdata):
            if l + k >= jumlahdata:
                break
            acfoutput[k] = acfoutput[k] + abs((data[k] ** 2) * numpy.exp(2j * numpy.pi * k * l / jumlahdata))
        acfoutput[k] = abs(acfoutput[k]) / jumlahdata

    ecgpeak=find_peaks(acfoutput, distance=100, height=0.1)[0]
    print(ecgpeak)

    plt.figure(5)
    plt.plot(numpy.arange(jumlahdata), data, label='Data RAW')
    plt.plot(numpy.arange(jumlahdata), acfoutput, label='ECG Correlation')

    peak=[acfoutput[k] for k in ecgpeak]
    plt.scatter(ecgpeak, peak, label='Peak')

    periodarray=[]
    for k in range(1, len(ecgpeak)):
        periodarray.append(ecgpeak[k]-ecgpeak[k-1])

    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")

    plt.figure(6)
    plt.bar(numpy.arange(len(periodarray)), periodarray, label=' ECG Period')
    plt.xlabel("Sequence")
    plt.ylabel("Period")
    plt.legend(loc="best")
    plt.show()


windows=Tk()
openbutton=Button(windows, text="Open File Text Data", command=inputdata).grid(row=0, columnspan=4)
acfbutton=Button(windows, text="Do AutoCorrelation", command=autocorrelation).grid(row=1, columnspan=4)
ccfbutton=Button(windows, text="Do CrossCorrelation", command=crosscorrelation).grid(row=2, column=0)
amplitudotkinter=StringVar(windows, value=1)
amplitudolabel=Label(windows, text="Amplitudo Gain = ").grid(row=2, column=1)
amplitudoinput=Entry(windows, textvariable=amplitudotkinter, width=4).grid(row=2, column=2)
noisetkinter=StringVar(windows, value=0.1)
noiselabel=Label(windows, text='Noise Gain =').grid(row=2, column=3)
noiseinput=Entry(windows, textvariable=noisetkinter, width=4).grid(row=2, column=4)
ecglabel=Label(windows, text='Check ECG Period *Must use the ECG input file').grid(row=4, columnspan=4)
ecgbutton=Button(windows, text="Find ECG Period", command=ecgperiod).grid(row=5, columnspan=4)
windows.mainloop()