#HEADER IMPORT ALL ITEM FROM TKINTER GUI

from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from matplotlib.figure import Figure

import math

import numpy


#DEKLARASI DATA AWAL
frek1 = 0
frek2 = 0
frek3 = 0
amp1 = 0.0
amp2 = 0.0
amp3 = 0.0
fc = 0
frek_sampling = 1000
waktu = 1
orde = 1

#DEKLARASI VARIABLE TAMBAHAN

xdata=[]
ydata=[]
ydata_filter=[]

#FUNGSI PROGRAM

def ambil_data_input():

    global frek1
    global frek2
    global frek3

    global amp1
    global amp2
    global amp3

    global fc

    global orde

    frek1=int(frek1_input.get())
    frek2=int(frek2_input.get())
    frek3=int(frek3_input.get())

    amp1=float(amp1_input.get())
    amp2=float(amp2_input.get())
    amp3=float(amp3_input.get())

    fc=int(fc_input.get())

    orde=int(orde_input.get())


def fungsi_sin(amp_local, frek_local, frek_sampling_local, n_local):
    periode_local=1/frek_sampling_local
    return amp_local*math.sin(2*math.pi*frek_local*periode_local*n_local)

def lpf_orde_1(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []

    periode_local = 1 / frek_sampling_local
    wc_local = 2*math.pi*fc_local

    ydata_local.insert(0, (wc_local*xdata_local[0])/((2/periode_local)+wc_local))

    for n in range(1, len(xdata_local)):
        ydata_local.insert(n, (((2/periode_local)-wc_local)*ydata_local[n-1]+wc_local*xdata_local[n]+wc_local*xdata_local[n-1])/((2/periode_local)+wc_local))

    return ydata_local

'''
def dft(data_local):
    e = 0
    e_real_local = 0
    e_imag_local = 0
    hasil = []

    for m in range (0, len(data_local)):
        for n in range (0, len(data_local)):
            e += data_local[n] * numpy.exp(-2j * numpy.pi * m * n / len(data_local))
            e_real_local += e.real
            e_imag_local += e.imag
        e = math.sqrt(math.pow(e.real,2)+math.pow(e.imag,2))
        hasil.insert(m, abs(e))
        e = 0

    print(hasil)

    return hasil

def idft(data_local):
    e = 0
    e_real_local = 0
    e_imag_local = 0
    hasil = []

    for m in range (0, len(data_local)):
        for n in range (0, len(data_local)):
            e += data_local[n] * numpy.exp(2j * numpy.pi * m * n / len(data_local))
            e_real_local += e.real
            e_imag_local += e.imag
        e = math.sqrt(math.pow(e.real, 2) + math.pow(e.imag, 2))
        e = e/len(data_local)
        hasil.insert(m, abs(e))
        e = 0

    print(hasil)

    return hasil

def lpf_orde_1(xdata_local, fc_local):
    xdata_filter_local = []
    w_cut_off_local = 2*math.pi*fc_local

    xdata_dft_local = dft(xdata_local)
    for n in range(0, len(xdata_local)):
        e = 1/(math.sqrt(1+(math.pow(xdata_dft_local[n]/w_cut_off_local,2))))
        xdata_filter_local.insert(n, abs(e))

    ydata_local = idft(xdata_filter_local)

    return xdata_filter_local

def lpf_orde_1(xdata_local, ydata_local, frek_sampling_local, fc_local):
    n = 0
    ydata_filter_local = []

    periode_local = 1 / frek_sampling_local
    alfa_local = periode_local/((1/(2*math.pi*fc_local)+periode_local))
    ydata_filter_local.insert(0, alfa_local*ydata_local[0])
    for i in xdata_local:
        n += 1
    for i in range(1, n):
        ydata_filter_local.insert(i, alfa_local*ydata_local[i] + (1-alfa_local)*ydata_filter_local[i-1])

    return ydata_filter_local
'''

def lpf_orde_2(xdata_local, frek_sampling_local, fc_local):
    ydata_local=[]
    a=[]
    b=[]
    c=0

    periode_local = 1 / frek_sampling_local
    wc_local = 2 * math.pi * fc_local
    a.insert(0, math.pow(wc_local,2)/((4/math.pow(periode_local,2))+(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2)))
    a.insert(1, 2*math.pow(wc_local,2)/((4/math.pow(periode_local,2))+(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2)))
    a.insert(2, math.pow(wc_local,2)/((4/math.pow(periode_local,2))+(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2)))
    b.insert(0, 0)
    b.insert(1, (8/math.pow(periode_local,2)-2*math.pow(wc_local,2))/((4/math.pow(periode_local,2))+(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2)))
    b.insert(2, -((4/math.pow(periode_local,2))-(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2))/((4/math.pow(periode_local,2))+(2*math.sqrt(2)*wc_local/periode_local)+math.pow(wc_local,2)))

    ydata_local.insert(0, a[0]*xdata_local[0])
    ydata_local.insert(1, b[1]*ydata_local[0]+a[0]*xdata_local[1]+a[1]*xdata_local[0])

    for n in range(2, len(xdata_local)):
        for m in range(1,3):
            c += b[m]*ydata_local[n-m]
        for m in range(0,3):
            c += a[m]*xdata_local[n-m]

        ydata_local.insert(n, c)
        c=0

    return ydata_local

def lpf_orde_3(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []
    a = []
    b = []
    d = 0

    periode_local = 1 / frek_sampling_local
    wc_local = 2 * math.pi * fc_local

    a.insert(0, math.pow(wc_local, 3))
    a.insert(1, 3*math.pow(wc_local, 3))
    a.insert(2, 3*math.pow(wc_local, 3))
    a.insert(3, math.pow(wc_local, 3))

    b.insert(0,0)
    b.insert(1, (24/math.pow(periode_local, 3))+(8/math.pow(periode_local, 2)*wc_local)-(4/periode_local*math.pow(wc_local,2))-(3*math.pow(wc_local, 3)))
    b.insert(2, -((24/math.pow(periode_local, 3))-(8/math.pow(periode_local, 2)*wc_local)-(4/periode_local*math.pow(wc_local, 2))+(3*math.pow(wc_local, 3))))
    b.insert(3, (8/math.pow(periode_local, 3))-(8/math.pow(periode_local, 2)*wc_local)+(4/periode_local*math.pow(wc_local, 2))-(math.pow(wc_local, 3)))

    c = (8/math.pow(periode_local, 3))+(8/math.pow(periode_local, 2)*wc_local)+(4/periode_local*math.pow(wc_local, 2))-(math.pow(wc_local, 3))

    ydata_local.insert(0, (a[0] * xdata_local[0]) / c)
    ydata_local.insert(1, (b[1] * ydata_local[0] + a[0] * xdata_local[1] + a[1] * xdata_local[0]) / c)
    ydata_local.insert(2, (b[2] * ydata_local[1] + b[1] * ydata_local[0] + a[0] * xdata_local[2] + a[1] * xdata_local[1] + a[2] * xdata_local[0]) / c)

    for n in range(3, len(xdata_local)):
        for m in range(1,4):
            d += (b[m]*ydata_local[n-m])/c
        for m in range(0,4):
            d += (a[m]*xdata_local[n-m])/c

        ydata_local.insert(n, d)
        d=0

    return ydata_local
'''
def lpf_orde_3(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []
    a = []
    b = []
    c = 0

    periode_local = 1 / frek_sampling_local
    wc_local = 2 * math.pi * fc_local

    b0.insert(0, 1 / ((8 * math.pow(frek_sampling_local, 3)) + (8 * wc_local * math.pow(frek_sampling_local, 2)) + (4 * math.pow(wc_local, 2) * frek_sampling_local) + math.pow(wc, 3)))
    for n in range(1, len(xdata_local)):
        a0 = (math.pow(wc_local, 3)*xdata_local[n])+(3*math.pow(wc_local, 3)*xdata_local[n-1])+(3*math.pow(wc_local, 3)*xdata_local[n-2])+(math.pow(wc_local, 3)*xdata_local[n-3])
        a1 = -(((-24)*math.pow(frek_sampling_local, 3)-(8*wc_local*math.pow(frek_sampling_local, 2))+(4*math.pow(wc_local, 2)*frek_sampling_local)+3*power(wc_local, 3))*ydata_local[n-1])
        a2 = -((24*power(frek_sampling_local, 3)-(8*wc_local*math.pow(frek_sampling_local, 2))-(4*math.pow(wc_local, 2)*frek_sampling_local)+3*math.pow(wc_local, 3)) * ydata_local[n-2])
        a3 = - (((-8)*math.pow(frek_sampling_local, 3) + (8*wc_local*math.pow(frek_sampling_local, 2))+(4*math.pow(wc, 2)*frek_sampling_local)+(math.pow(wc_local, 3)))*ydata_local[n - 3])


    

    print(ydata_local)

    return ydata_local


def lpf_orde_3(xdata_local, frek_sampling_local, fc_local):
    ydata_local = []
    a = []
    b = []
    c = 0

    periode_local = 1 / frek_sampling_local
    wc_local = 2 * math.pi * fc_local

    a.insert(0, (math.pow(wc_local,2))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    a.insert(1, (3*math.pow(wc_local,2))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    a.insert(2, (3*math.pow(wc_local,2))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    a.insert(3, (math.pow(wc_local,2))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    b.insert(0, 0)
    b.insert(1, ((-24/math.pow(periode_local,3))+(3*math.pow(wc_local,3)))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    b.insert(2, ((24/math.pow(periode_local,3))-(8/math.pow(periode_local,2))+(4/periode_local)+(3*math.pow(wc_local,3)))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))
    b.insert(3, ((-8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))-(4/periode_local)+math.pow(wc_local,3))/((8/math.pow(periode_local,3))+(8/math.pow(periode_local,2))+(4/periode_local)+math.pow(wc_local,3)))

    ydata_local.insert(0, a[0]*xdata_local[0])
    ydata_local.insert(1, b[1]*ydata_local[0]+a[0]*xdata_local[1]+a[1]*xdata_local[0])
    ydata_local.insert(2, b[1]*ydata_local[1]+b[2]*ydata_local[0]+a[0]*xdata_local[2]+a[1]*xdata_local[1]+a[2]*xdata_local[0])
    ydata_local.insert(3, b[1]*ydata_local[2]+b[2]*ydata_local[1]+b[3]*ydata_local[0]+a[0]*xdata_local[3]+a[1]*xdata_local[2]+a[2]*xdata_local[1]+a[3]*xdata_local[0])


    for n in range(4, len(xdata_local)):
        for m in range(1,4):
            c += b[m]*ydata_local[n-m]
        for m in range(0,4):
            c += a[m]*xdata_local[n-m]

        ydata_local.insert(n, c)
        c = 0

    print(ydata_local)


    return ydata_local
'''


def proses_input():
    xdata.clear()
    ydata.clear()

    ambil_data_input()

    for n in range(0, waktu*frek_sampling):
        xdata.insert(n, n)
        ydata.insert(n, fungsi_sin(amp1, frek1, frek_sampling, n) + fungsi_sin(amp2, frek2, frek_sampling, n) + fungsi_sin(amp3, frek3, frek_sampling, n))

    grafik1.clear()
    grafik1.add_subplot(111).plot(xdata, ydata)
    grafik1_windows.draw()

def proses_output():
    ambil_data_input()

    if orde == 1:
        #ydata_filter = lpf_orde_1(xdata, ydata, frek_sampling, fc)
        ydata_filter = lpf_orde_1(ydata, frek_sampling, fc)
    elif orde == 2:
        ydata_filter = lpf_orde_2(ydata, frek_sampling, fc)
    elif orde == 3:
        ydata_filter = lpf_orde_3(ydata, frek_sampling, fc)

    grafik2.clear()
    grafik2.add_subplot(111).plot(xdata, ydata_filter)
    grafik2_windows.draw()

    ydata_filter.clear()

#MEMBUAT WINDOW JENDELA DAN GRAFIK

windows=Tk()

grafik1 = Figure(figsize=(5,2))

grafik2 = Figure(figsize=(5,2))

grafik1_windows = FigureCanvasTkAgg(grafik1, windows)

grafik2_windows = FigureCanvasTkAgg(grafik2, windows)


#DEFINISIKAN LABEL PADA WINDOW

l1=Label(windows, text='Frekuensi 1')
l1.grid(row=0, column=0)

l2=Label(windows, text='Frekuensi 2')
l2.grid(row=0, column=2)

l3=Label(windows, text='Frekuensi 3')
l3.grid(row=0, column=4)

l4=Label(windows, text='Amplitudo 1')
l4.grid(row=1, column=0)

l5=Label(windows, text='Amplitudo 2')
l5.grid(row=1, column=2)

l6=Label(windows, text='Amplitudo 3')
l6.grid(row=1, column=4)

l7=Label(windows, text='Frek Cutoff')
l7.grid(row=4, column=0)

#DEFINISI INPUT TEXT STRING

frek1_input = StringVar()
e1=Entry(windows, textvariable=frek1_input, width=8)
e1.insert(0, 5)
e1.grid(row=0, column=1)

frek2_input = StringVar()
e2=Entry(windows, textvariable=frek2_input, width=8)
e2.insert(0, 46)
e2.grid(row=0, column=3)

frek3_input = StringVar()
e3=Entry(windows, textvariable=frek3_input, width=8)
e3.insert(0, 99)
e3.grid(row=0, column=5)

amp1_input = StringVar()
e4=Entry(windows, textvariable=amp1_input, width=8)
e4.insert(0, 1)
e4.grid(row=1, column=1)

amp2_input = StringVar()
e5=Entry(windows, textvariable=amp2_input, width=8)
e5.insert(0, 0.2)
e5.grid(row=1, column=3)

amp3_input = StringVar()
e6=Entry(windows, textvariable=amp3_input, width=8)
e6.insert(0, 0.02)
e6.grid(row=1, column=5)

fc_input = StringVar()
e7=Entry(windows, textvariable=fc_input, width=8)
e7.insert(0, 5)
e7.grid(row=4, column=1)

#DEFINISI INPUT BUTTON

b1=Button(windows, text='PLOT INPUT', command=proses_input)
b1.grid(row=0, column=6, rowspan=2)

b2=Button(windows, text='PLOT OUTPUT', command=proses_output)
b2.grid(row=4, column=6)


#MEMASANG AREA GRAFIK PADA WINDOWS

grafik1_windows.get_tk_widget().grid(row=3, column=0, columnspan=7)

grafik2_windows.get_tk_widget().grid(row=5, column=0, columnspan=7)

#RADIO BUTTON

orde_input=IntVar()

r1=Radiobutton(windows, text='Orde1', value=1, variable=orde_input)
r1.grid(row=4, column=3)

r2=Radiobutton(windows, text='Orde2', value=2, variable=orde_input)
r2.grid(row=4, column=4)

r3=Radiobutton(windows, text='Orde3', value=3, variable=orde_input)
r3.grid(row=4, column=5)

windows.mainloop()
