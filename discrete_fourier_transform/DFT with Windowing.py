import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)

from matplotlib.figure import Figure

import numpy

from tkinter.filedialog import askopenfilename

import math

def fungsi(n):
    return 2*numpy.sin(2000*numpy.pi*n/8000)

def _quit():
    root.quit()
    root.destroy()

def c_open_file():
    rep = askopenfilename(parent=root)
    print(rep)
    global ndata
    global xdata
    global ydata

    f = open(rep, 'r')
    data = f.readlines()
    n = 0
    xdata = []
    ydata = []

    for a in data:
        aa = a.replace('\n', '')
        aaa = aa.split('\t')
        xdata.insert(n, int(aaa[0]))
        ydata.insert(n, int(aaa[1]))
        n += 1

    ndata = n
    plotdata(xdata, ydata)

def plotdata(x , y):
    fig.add_subplot(121).bar(x, y, width=0.05)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, expand=1)

def plotdata1(x, y):
    fig.add_subplot(122).bar(x, y, width=0.05)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, expand=1)

def clearplot():
    fig.clear()
    canvas.draw()

def plotgrafik(x, y):
    fig.add_subplot(121).bar(x, y, width=0.8)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, expand=1)

def plotgrafik1(x, y):
    fig.add_subplot(122).bar(x, y, width=0.8)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, expand=1)

def plotdft(jumlahdata, data):
    e = 0
    hasil = []
    hasilreal = []
    hasilimag = []
    xreal = []
    ximag = []

    for m in range (0, jumlahdata):
        for n in range (0, jumlahdata):
            e += data[n] * numpy.exp(-2j * numpy.pi * m * n / jumlahdata)
        hasil.insert(m, math.sqrt(math.pow(e.real, 2)+math.pow(e.imag, 2)))
        #hasil.insert(m, e)
        hasilreal.insert(m, e.real)
        hasilimag.insert(m, e.imag)
        xreal.insert(m, m)
        ximag.insert(m, m/jumlahdata)
        e = 0
    #plotdata(xreal, hasil)
    #plotdata(xreal, hasilreal)
    #plotdata(ximag, hasilimag)

    return hasil, xreal

def plotidft(jumlahdata, data):
    e = 0
    hasil = []
    hasilreal = []
    hasilimag = []
    xreal = []
    ximag = []

    for m in range (0, jumlahdata):
        for n in range (0, jumlahdata):
            e += data[n] * numpy.exp(2j * numpy.pi * m * n / jumlahdata)
        e = e/jumlahdata
        hasil.insert(m, math.sqrt(math.pow(e.real, 2) + math.pow(e.imag, 2)))
        #hasil.insert(m, e)
        hasilreal.insert(m, e.real)
        hasilimag.insert(m, e.imag)
        xreal.insert(m, m)
        ximag.insert(m, m/jumlahdata)
    #plotdata1(xreal, hasil)
    #plotdata1(xreal, hasilreal)
    #plotdata1(ximag, hasilimag)

    return hasil, xreal

def plotfile():
    fig.clear()
    e, x = plotdft(ndata, ydata)
    plotdata(x, e)
    e1, x1 = plotidft(ndata, e)
    plotdata1(x1, e1)

def plotfungsi50():
    windowsize = 50
    c = []
    c1 = []
    for n in range(0, windowsize):
        c1.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000))
        c.insert(n, n)

    plotgrafik(c, c1)
    e, x = plotdft(windowsize, c1)
    plotgrafik1(x, e)

def plotfungsi100():
    windowsize = 100
    c = []
    c1 = []
    for n in range(0, windowsize):
        c1.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000))
        c.insert(n, n)

    plotgrafik(c, c1)
    e, x = plotdft(windowsize, c1)
    plotgrafik1(x, e)

def plotfungsi150():
    windowsize = 150
    c = []
    c1 = []
    for n in range(0, windowsize):
        c1.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000))
        c.insert(n, n)

    plotgrafik(c, c1)
    e, x = plotdft(windowsize, c1)
    plotgrafik1(x, e)

def plottriangular():
    windowsize = 50
    plotwtri = []
    x = []
    data = []

    for n in range(0, windowsize):
        wtri = 1 - ((abs(2 * n - windowsize + 1)) / (windowsize - 1))
        plotwtri.insert(n, wtri)
        x.insert(n, n)
    #print(x, plotwtri)
    #plotgrafik(x, plotwtri)

    x = []
    for n in range(0, windowsize):
        wtri = 1 - ((abs(2*n - windowsize + 1))/(windowsize - 1))
        data.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000) * wtri)
        x.insert(n, n)

    e, x = plotdft(windowsize, data)
    plotgrafik(x, data)
    plotgrafik1(x, e)

def plothamming():
    windowsize = 100
    plotwham = []
    x = []
    data = []

    for n in range(0, windowsize):
        wham = 0.54 - 0.46*numpy.cos((2*numpy.pi*n)/(windowsize-1))
        plotwham.insert(n, wham)
        x.insert(n, n)
    #print(x, plotwham)
    #plotgrafik(x, plotwham)

    x = []
    for n in range(0, windowsize):
        wham = 0.54 - 0.46*numpy.cos((2*numpy.pi*n)/(windowsize-1))
        data.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000) * wham)
        x.insert(n, n)

    e, x = plotdft(windowsize, data)
    plotgrafik(x, data)
    plotgrafik1(x, e)

def plothanning():
    windowsize = 150
    plotwhan = []
    x = []
    data = []

    #for n in range(0, windowsize):
    #    whan = 0.5 - 0.5 * numpy.cos((2 * numpy.pi * n) / (windowsize - 1))
    #    plotwhan.insert(n, whan)
    #    x.insert(n, n)
    #print(x, plotwhan)
    #plotgrafik(x, plotwhan)

    x = []
    for n in range(0, windowsize):
        whan = 0.5 - 0.5 * numpy.cos((2 * numpy.pi * n) / (windowsize - 1))
        data.insert(n, 2 * numpy.sin(2000 * numpy.pi * n / 8000) * whan)
        x.insert(n, n)

    e, x = plotdft(windowsize, data)
    plotgrafik(x, data)
    plotgrafik1(x, e)


#DEKLARASI VARIABLE GLOBAL

fs = 8000

#FUNGSIJENDELAWINDOWS

root = tkinter.Tk()
fig = Figure(figsize=(8,3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)

x = tkinter.Button(master=root, text='OPEN FILE', command=c_open_file)
x.pack()

x1 = tkinter.Button(master=root, text='Plot DFT', command=plotfile)
x1.pack()

x2 = tkinter.Button(master=root, text='FUNCTION PLOT Windows Size 50 Dengan DFT', command=plotfungsi50)
x2.pack()

x3 = tkinter.Button(master=root, text='FUNCTION PLOT Windows Size 100 Dengan DFT', command=plotfungsi100)
x3.pack()

x4 = tkinter.Button(master=root, text='FUNCTION PLOT Windows Size 150 Dengan DFT', command=plotfungsi150)
x4.pack()

x5 = tkinter.Button(master=root, text='Plot Triangular Windows Function', command=plottriangular)
x5.pack()

x6 = tkinter.Button(master=root, text='Plot Hamming Windows Function', command=plothamming)
x6.pack()

x7 = tkinter.Button(master=root, text='Plot Hanning Windows Function', command=plothanning)
x7.pack()

x8 = tkinter.Button(master=root, text='Clear', command=clearplot)
x8.pack()

tkinter.mainloop()
