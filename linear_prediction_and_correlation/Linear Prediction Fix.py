from tkinter import *
import numpy
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

data=[]
jumlahdata=0
frekuensisampling=200
acfoutput = numpy.zeros(jumlahdata)

def sinusoidalfunctiongenerator():
    global jumlahdata
    global data

    frek1 = int(frek1_input.get())
    frek2 = int(frek2_input.get())
    frek3 = int(frek3_input.get())
    amp1 = float(amp1_input.get())
    amp2 = float(amp2_input.get())
    amp3 = float(amp3_input.get())
    jumlahdata = int(jumlahdata_input.get())

    for a in range(jumlahdata):
        sinus1 = amp1 * numpy.sin(2 * numpy.pi * frek1 * a / frekuensisampling)
        sinus2 = amp2 * numpy.sin(2 * numpy.pi * frek2 * a / frekuensisampling)
        sinus3 = amp3 * numpy.sin(2 * numpy.pi * frek3 * a / frekuensisampling)
        data.append(sinus1 + sinus2 + sinus3)

    plt.figure(1)
    plt.plot(numpy.arange(jumlahdata), data, label='Plot Sinusoidal Input Data')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

def opentextfilefunction():
    global jumlahdata
    global data

    Tk().withdraw()
    filename = askopenfilename()
    function = open(filename, 'r')
    data = function.readlines()

    # Turning The Raw Data to Valid Data
    for i in range(0, len(data)):
        data[i] = float(data[i].replace('\n', ''))
    jumlahdata = len(data)

    plt.figure(2)
    plt.plot(numpy.arange(jumlahdata), data, label='Plot Text File Input Data')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

def autocorrelationfunction():
    global acfoutput
    acfoutput = numpy.zeros(jumlahdata)

    for k in range(jumlahdata):
        for l in range(jumlahdata):
            if l + k >= jumlahdata:
                break
            acfoutput[k] = acfoutput[k] + abs((data[k] ** 2) * numpy.exp(2j * numpy.pi * k * l / jumlahdata))
        acfoutput[k] = abs(acfoutput[k]) / jumlahdata

    plt.figure(3)
    plt.plot(numpy.arange(jumlahdata), acfoutput, label='Plot Auto Correlation')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

def linearpredictionfunction():
    lpoutput = numpy.zeros(jumlahdata)
    err = numpy.zeros(jumlahdata)
    temp = 0
    alfa = int(alfa_input.get())
    r = numpy.zeros((jumlahdata, jumlahdata))

    err[0]=1
    for a in range(1, alfa+1):
        for b in range(1, a):
            temp = temp + r[b][a-1] * acfoutput[a-b]
        r[a][a] = (acfoutput[a] - temp)/err[a-1]
        if a > 1:
            for b in range(1, a-1):
                r[b][a] = r[b][a-1] - r[a][a]*r[a-b][a-1]
        err[a] = (1-(r[a][a])**2)*err[a-1]

    for a in range(1, jumlahdata):
        for b in range(1, alfa+1):
            lpoutput[a] = lpoutput[a] + r[a][alfa]*data[a-b]

    print(lpoutput)

    plt.figure(4)
    plt.plot(numpy.arange(jumlahdata), lpoutput, label='Plot Linear Prediction')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")

    plt.figure(5)
    plt.plot(numpy.arange(jumlahdata), err, label='Error Plot Linear Prediction')
    plt.xlabel("Sequence")
    plt.ylabel("Amplitudo")
    plt.legend(loc="best")
    plt.show()

#DEFINISIKAN LABEL PADA WINDOW

windows = Tk()
judullabel=Label(windows, text='Linear Prediction Models').grid(row=0, column=0, columnspan=6)
f1label=Label(windows, text='Frekuensi 1').grid(row=1, column=0)
f2label=Label(windows, text='Frekuensi 2').grid(row=1, column=1)
f3=Label(windows, text='Frekuensi 3').grid(row=1, column=2)
a1label=Label(windows, text='Amplitudo 1').grid(row=1, column=3)
a2label=Label(windows, text='Amplitudo 2').grid(row=1, column=4)
a3=Label(windows, text='Amplitudo 3').grid(row=1, column=5)
jumlahdatalabel=Label(windows, text='Fs = 200 Hz, Jumlah Data').grid(row=3, column=4)
alfalabel=Label(windows, text='Alfa').grid(row=6, column=4)

#DEFINISI INPUT TEXT STRING

frek1_input = StringVar()
f1entry=Entry(windows, textvariable=frek1_input, width=8)
f1entry.insert(0, 5)
f1entry.grid(row=2, column=0)

frek2_input = StringVar()
f2entry=Entry(windows, textvariable=frek2_input, width=8)
f2entry.insert(0, 46)
f2entry.grid(row=2, column=1)

frek3_input = StringVar()
f3entry=Entry(windows, textvariable=frek3_input, width=8)
f3entry.insert(0, 99)
f3entry.grid(row=2, column=2)

amp1_input = StringVar()
a1entry=Entry(windows, textvariable=amp1_input, width=8)
a1entry.insert(0, 1)
a1entry.grid(row=2, column=3)

amp2_input = StringVar()
a2entry=Entry(windows, textvariable=amp2_input, width=8)
a2entry.insert(0, 0.2)
a2entry.grid(row=2, column=4)

amp3_input = StringVar()
a3entry=Entry(windows, textvariable=amp3_input, width=8)
a3entry.insert(0, 0.02)
a3entry.grid(row=2, column=5)

jumlahdata_input = StringVar()
jumlahdataentry=Entry(windows, textvariable=jumlahdata_input, width=8)
jumlahdataentry.insert(0, 500)
jumlahdataentry.grid(row=3, column=5)

alfa_input = StringVar()
alfaentry=Entry(windows, textvariable=alfa_input, width=8)
alfaentry.insert(0, 4)
alfaentry.grid(row=6, column=5)
#DEFINISI INPUT BUTTON

b1=Button(windows, text='Pilih Data dari Generator Sinyal Sinus', command=sinusoidalfunctiongenerator).grid(row=3, columnspan=3)
b2=Button(windows, text='Pilih Data dari File External', command=opentextfilefunction).grid(row=4, columnspan=6)
b3=Button(windows, text='Plot Auto Correlation', command=autocorrelationfunction).grid(row=5, columnspan=6)
b1=Button(windows, text='Plot Linear Prediction', command=linearpredictionfunction).grid(row=6, columnspan=3)

windows.mainloop()
