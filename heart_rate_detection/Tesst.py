from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from matplotlib.pyplot import Circle
import numpy as np
import math as mt
from tkinter.filedialog import askopenfilename
from matplotlib.pylab import show
import matplotlib.animation as animation

# MEMBUAT WINDOW JENDELA DAN GRAFIK
windows = Tk()


class Plot:
    def __init__(self, id, x, y, kondisi, color):
        self.id = id
        self.x = x
        self.y = y
        self.kondisi = kondisi
        self.color = color


class Axis:
    def __init__(self, judul, labelx, labely, row, column, rowspan, columnspan, tipe):
        self.labelx = labelx
        self.labely = labely
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.title = judul
        self.tipe = tipe
        if self.tipe == 0:
            self.fig = Figure(figsize=(6, 1.1))
        else:
            self.fig = Figure(figsize=(2.4, 1.1))
        self.grafik_windows = FigureCanvasTkAgg(self.fig, windows)
        self.ax = self.fig.add_subplot(111)
        self.grafik_windows.get_tk_widget().grid(row=self.row,
                                                 column=self.column,
                                                 rowspan=self.rowspan,
                                                 columnspan=self.columnspan)

        self.ax.set_title(self.title, fontsize=8)
        self.ax.set_xlabel(self.labelx, fontsize=8)
        self.ax.set_ylabel(self.labely, fontsize=8)
        self.ax.tick_params(direction='in', labelsize=6)
        box = self.ax.get_position()
        if self.tipe == 0:
            self.ax.set_position([box.x0 - box.width * 0.07, box.y0 + box.height * 0.18,
                                  box.width * 1.15, box.height * 0.75])
        else:
            self.ax.set_position([box.x0 + box.width * 0.07, box.y0 + box.height * 0.18,
                                  box.width * 0.935, box.height * 0.75])

    def draw_plot(self):
        self.ax.clear()
        self.__init__(self.title, self.labelx, self.labely, self.row,
                      self.column, self.rowspan, self.columnspan, self.tipe)
        for item in self.plotlist:
            if item.kondisi == 0:
                self.ax.plot(item.x, item.y, color=item.color, linewidth=0.5)
            elif item.kondisi == 1:
                self.ax.bar(item.x, item.y, color=item.color, linewidth=0.5)
        self.grafik_windows.draw()

    def plot(self, x, y, kondisi=0, color='b'):
        self.plotlist = []
        self.add_plot(0, x, y, kondisi, color)

    def add_plot(self, id, x, y, kondisi=0, color='b'):
        for i, item in enumerate(self.plotlist):  # Jika ada plot dengan id yg sama
            if item.id == id:
                self.plotlist[i] = Plot(id, x, y, kondisi, color)
                self.draw_plot()
                return

        self.plotlist += [Plot(id, x, y, kondisi, color)]  # Jika belum ada plot dengan id yang ditentukan
        self.draw_plot()

    def simulation(self, ws, x, y, color='blue'):
        self.ax.set_ylim(min(y) - 0.2, max(y) + 0.2)
        self.ax.set_xlim(0, ws)
        self.t1 = 0
        self.enum = 0
        self.t = np.arange(ws)
        self.yp = np.zeros([ws])
        self.y_sim = np.zeros([ws])
        self.p1, = self.ax.plot([], [], color=color, linewidth=0.5)
        self.p2, = self.ax.plot([], [], color=color, linewidth=0.5)
        self.grafik_windows.draw()
        self.pause = False

        def onClick(event):
            self.pause ^= True

        def animasigerak(num):
            global y
            global x

            if not self.pause:
                self.yp[self.t1] = y[self.enum]

                if self.t1 >= ws - 1:
                    self.t1 = 0

                if self.enum >= np.size(y) - 1:
                    self.enum = 0

                self.p1.set_data(self.t[0:self.t1], self.yp[0:self.t1])
                self.p2.set_data(self.t[self.t1 + 10:ws], self.yp[self.t1 + 10:ws])

                self.y_sim = np.concatenate((self.yp[self.t1 + 1:ws - 1], self.yp[0:self.t1]))
                yBPF = BPF(self.y_sim)
                yDRV = DRV(yBPF)
                ySQR = SQR(yDRV)
                yMVI, th = MVI(ySQR)
                y_peak = Peak(yMVI, th)
                RtoR = RR(y_peak)
                Miss_3, Miss_4 = Hitung(RtoR)
                e4.delete(0, END)
                e5.delete(0, END)
                e4.insert(0, Miss_3)
                e5.insert(0, Miss_4)

                self.t1 += 1
                self.enum += 1

            return self.p1, self.p2

        line_ani = animation.FuncAnimation(self.fig, animasigerak, frames=len(y), interval=2, blit=True, repeat=True)
        self.fig.canvas.mpl_connect('button_press_event', onClick)

        show()


class Axis2:
    def __init__(self, judul, labelx, labely, row, column, rowspan, columnspan):
        self.labelx = labelx
        self.labely = labely
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.title = judul
        self.fig = Figure(figsize=(2.4, 1.1))
        self.grafik_windows = FigureCanvasTkAgg(self.fig, windows)
        self.ax = self.fig.add_subplot(111)
        self.grafik_windows.get_tk_widget().grid(row=self.row,
                                                 column=self.column,
                                                 rowspan=self.rowspan,
                                                 columnspan=self.columnspan)

        self.ax.set_xlim((-1.05, 1.05))
        self.ax.set_ylim((-1.05, 1.05))

        self.Circle = Circle((0, 0), 1, color='black', fill=False)
        self.ax.text(-2.375, 1.1, self.title, fontsize=8)
        self.ax.text(1.1, 0, self.labelx, fontsize=8)
        self.ax.text(0, 1.1, self.labely, fontsize=8)
        self.ax.add_artist(self.Circle)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.spines['left'].set_position(('data', 0))
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['right'].set_color(('none'))
        self.ax.spines['top'].set_color(('none'))

        box = self.ax.get_position()
        self.ax.set_position([box.x0 + box.width * 0.25, box.y0 - box.height * 0.1,
                              box.width * 0.55, box.height * 1.1])

    def draw_plot(self):
        self.ax.clear()
        self.__init__(self.title, self.labelx, self.labely, self.row,
                      self.column, self.rowspan, self.columnspan)
        for item in self.plotlist:
            if item.kondisi == 0:
                self.ax.scatter(item.x, item.y, color=item.color, marker='o')
            elif item.kondisi == 1:
                self.ax.scatter(item.x, item.y, color=item.color, marker='x')
        self.grafik_windows.draw()

    def plot(self, x, y, kondisi=0, color='b'):
        self.plotlist = []
        self.add_plot(0, x, y, kondisi, color)

    def add_plot(self, id, x, y, kondisi=0, color='b'):
        for i, item in enumerate(self.plotlist):  # Jika ada plot dengan id yg sama
            if item.id == id:
                self.plotlist[i] = Plot(id, x, y, kondisi, color)
                self.draw_plot()
                return

        self.plotlist += [Plot(id, x, y, kondisi, color)]  # Jika belum ada plot dengan id yang ditentukan
        self.draw_plot()


# MENEMPELKAN AREA GRAFIK PADA WINDOWS
ax1 = Axis("Sinyal ECG", 'n', 'x[n]', 3, 1, 4, 5, 0)
ax2 = Axis("Windowing", 'n', 'x[n]', 8, 1, 4, 2, 1)
ax3 = Axis("Frekuensi Spektrum", 'Hz', 'A', 8, 4, 4, 2, 1)
ax4 = Axis2("z-plane", r'$Re(z)$', r'$Im(z)$', 13, 1, 4, 2)
ax5 = Axis("Frekuensi Spektrum", 'Hz', 'A', 13, 4, 4, 2, 1)
ax6 = Axis("Band Pass Filter", 'n', 'x[n]', 3, 7, 4, 5, 0)
ax7 = Axis("Derivative", 'n', 'x[n]', 8, 7, 4, 5, 0)
ax8 = Axis("Square", 'n', 'x[n]', 13, 7, 4, 5, 0)
ax9 = Axis("Moving Window Integration", 'n', 'x[n]', 18, 7, 4, 5, 0)
ax10 = Axis("PUNCAK PUNCAK", 'n', 'x[n]', 23, 7, 4, 5, 0)
ax11 = Axis("Simulation", 'n', 'x[n]', 18, 1, 4, 5, 0)

# JUDUL WINDOW
font9 = "-family {Showcard Gothic} -size 20 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"
title = Label(windows, text="Heartrate Detection", font=font9)
title.grid(row=0, column=3, columnspan=7)


def spin_init():
    spin1.__setitem__('from_', 0)
    spin1.__setitem__('to', N)
    spin2.__setitem__('from_', 0)
    spin2.__setitem__('to', N)


def all_init():
    spin_init()
    ax2.ax.clear()
    ax3.ax.clear()
    ax4.ax.clear()
    ax5.ax.clear()
    ax6.ax.clear()
    ax7.ax.clear()
    ax8.ax.clear()
    ax9.ax.clear()
    ax10.ax.clear()
    ax11.ax.clear()


# input
def awal():
    global N, n, y, fs

    # baca file
    rep = askopenfilename(parent=windows)
    print(rep)

    f = open(rep, "r")
    input = f.readlines()

    n, y = [], []
    for i, a in enumerate(input):
        if i == 0:
            continue
        elif i == 1:
            b = a.replace('(', '')
            c = b.replace(' sec)', '')
            d = c.split('\t')
            fs = (1 / float(d[0]))
            continue
        aa = a.replace('\n', '')
        aaa = aa.split('\t')
        n += [float(aaa[0])]
        y += [float(aaa[1])]

    N = np.size(n)

    all_init()
    ax1.plot(n, y, 0)
    e1.delete(0, END)
    e1.insert(0, fs)


# Discrete Fourier Transform
def DFT(yy):
    n = np.size(yy)
    DFT_r = np.zeros([n])
    DFT_i = np.zeros([n])
    y_data = np.zeros([n])
    for i in range(n):
        for j in range(n):
            a_1 = yy[j] * mt.cos((2 * np.pi * i * j) / n)
            a_2 = -(yy[j] * mt.sin((2 * np.pi * i * j) / n))
            DFT_r[i] += a_1
            DFT_i[i] += a_2
        y_data[i] = (mt.sqrt((DFT_r[i] ** 2) + (DFT_i[i] ** 2))) / n
    return y_data


def Hanning():
    global yHann
    s1 = int(spin1.get())
    s2 = int(spin2.get())
    index = 0

    yHann = np.zeros([N])
    for i in range(s1, s2):
        yHann[i] = (0.5 - (0.5 * mt.cos((2 * np.pi * index) / ((s2 - s1) - 1))))
        index += 1
    ax1.add_plot(4, n, yHann, color='red')
    ax1.add_plot(5, [s1, s1], [0, max(y)], 0, 'red')
    ax1.add_plot(6, [s2, s2], [0, max(y)], 0, 'red')
    ax2.plot(n[s1:s2], y[s1:s2])


def Windowing():
    global yWindow

    yWindow = []
    for i in range(N):
        yWindow += [y[i] * yHann[i]]

    yDFT = DFT(yWindow)
    ax3.plot(np.arange(int(np.size(yDFT) / 2)),
             yDFT[0:int(np.size(yDFT) / 2)], 0)


def pole_zero():
    global r_p, x_p

    r_p = float(spin3.get())
    s_p = int(spin4.get())

    x_p = r_p * mt.cos((s_p * np.pi) / 360)
    y1 = r_p * mt.sin((s_p * np.pi) / 360)
    y2 = -r_p * mt.sin((s_p * np.pi) / 360)

    f_resp = []
    for i in range(int(N / 2)):
        w = (2 * np.pi * i) / N
        num = mt.sqrt((1 - mt.cos(2 * w)) ** 2 + (mt.sin(2 * w)) ** 2)
        denum = mt.sqrt((1 - 2 * x_p * mt.cos(w) + (r_p ** 2) * mt.cos(2 * w)) ** 2 + (
                    2 * x_p * mt.sin(w) - (r_p ** 2) * mt.sin(2 * w)) ** 2)
        f_resp += [num / denum]

    ax4.plot([-1, 1], [0, 0])
    ax4.add_plot(1, [x_p, x_p], [y1, y2], 1)
    ax5.plot(np.arange(N / 2), f_resp)


# BPF
def BPF(non_filtered):
    yBPF = np.zeros(np.size(non_filtered))
    for i in range(np.size(non_filtered)):
        yBPF[i] += 2 * x_p * yBPF[i - 1] - (r_p ** 2) * yBPF[i - 2] + non_filtered[i]
        if i > 2: yBPF[i] += -non_filtered[i - 2]

    if np.amax(yBPF) > 1:
        yBPF = yBPF / np.amax(yBPF)  # agar tidak terjadi gain

    return yBPF


def DRV(yBPF):
    yDRV = []
    for i in range(np.size(yBPF)):
        if i < 2:
            a = 0
        else:
            a = -yBPF[i - 2]
        if i < 1:
            b = 0
        else:
            b = -2 * yBPF[i - 1]
        if i > np.size(yBPF) - 2:
            c = 0
        else:
            c = 2 * yBPF[i + 1]
        if i > np.size(yBPF) - 3:
            d = 0
        else:
            d = yBPF[i + 2]
        yDRV += [(a + b + c + d) / 8]

    if np.amax(yDRV) > 1:
        yDRV = yDRV / np.amax(yDRV)  # agar tidak terjadi gain

    return yDRV


# Squaring
def SQR(yDRV):
    ySQR = list(map(lambda x: x ** 2, yDRV))

    return ySQR


# LPF kedua
def MVI(ySQR):
    yMVI = []
    WSI = 30
    for i in range(np.size(ySQR)):
        MAV = 0
        for j in range(WSI):
            if i - (WSI - j) >= 0:
                MAV += ySQR[i - (WSI - j)]
        yMVI += [MAV / WSI]

    spki, npki, th = np.zeros([np.size(yMVI)]), np.zeros([np.size(yMVI)]), np.zeros([np.size(yMVI)])
    for i in range(np.size(yMVI)):
        spki[i] = 0.125 * max(yMVI) + 0.875 * spki[i - 1]
        npki[i] = 0.125 * max(yMVI) + 0.875 * npki[i - 1]
        th[i] = 0.5 * (npki[i] + 0.25 * (spki[i] - npki[i]))

    return yMVI, th


def Peak(yMVI, th):  # menentukan peak detector
    y_peak = np.zeros([np.size(yMVI)])

    HR_data = yMVI
    maxvalue = 0
    n_maxvalue = 0
    status = 0
    for i in range(1, len(HR_data) - 1):
        if HR_data[i] > th[i] and HR_data[i] > HR_data[i - 1] and HR_data[i] > HR_data[i + 1]:
            if HR_data[i] > maxvalue:
                maxvalue = HR_data[i]
                n_maxvalue = i
                status = 1
        if HR_data[i] < th[i]:
            if status == 1:
                y_peak[n_maxvalue] = maxvalue
                status = 0
                maxvalue = 0

    return y_peak


def RR(y_peak):
    R = []
    RtoR = []
    for i in range(np.size(y_peak)):
        if y_peak[i] != 0:
            R += [i]

    if np.size(R) <= 1:
        return [0]
    else:
        for i in range(int(np.size(R) - 1)):
            RtoR += [R[i + 1] - R[i]]
        return RtoR


def Hitung(RtoR):
    Miss_1 = np.mean(RtoR)
    if Miss_1 == 0:
        Miss_2 = 0
    else:
        Miss_2 = (fs * 60) / Miss_1
    return Miss_1, Miss_2


def Generate():
    global Miss_1, Miss_2

    yBPF = BPF(y)
    ax6.plot(n, yBPF)

    yDRV = DRV(yBPF)
    ax7.plot(n, yDRV)

    ySQR = SQR(yDRV)
    ax8.plot(n, ySQR)

    yMVI, th = MVI(ySQR)
    ax9.plot(n, yMVI)
    ax9.add_plot(1, n, th, color='red')

    y_peak = Peak(yMVI, th)
    ax10.plot(n, y_peak)

    RtoR = RR(y_peak)

    Miss_1, Miss_2 = Hitung(RtoR)


def Result_Show():
    e2.delete(0, END)
    e3.delete(0, END)
    e2.insert(0, Miss_1)
    e3.insert(0, Miss_2)


def Simulation():
    ws = int(4 * fs)
    ax11.simulation(ws, n, y)


# DEFINISIKAN LABEL PADA WINDOW
l1 = Label(windows, text='Frekuensi Sampling\t=')
l1.grid(row=2, column=1, columnspan=2)
l2 = Label(windows, text='R to R =')
l2.grid(row=25, column=1)
l3 = Label(windows, text='Heartrate =')
l3.grid(row=26, column=1)
l4 = Label(windows, text='R to R =')
l4.grid(row=25, column=4)
l44 = Label(windows, text='Heartrate =')
l44.grid(row=26, column=4)
l5 = Label(windows, text='↓')
l5.grid(row=22, column=9)
l6 = Label(windows, text='↓')
l6.grid(row=17, column=9)
l7 = Label(windows, text='↓')
l7.grid(row=12, column=9)
l8 = Label(windows, text='↓')
l8.grid(row=7, column=9)
l9 = Label(windows, text=' ', fg="white")
l9.grid(row=2, column=0, rowspan=25)
l10 = Label(windows, text=' ')
l10.grid(row=2, column=6, rowspan=25)
l11 = Label(windows, text=' ')
l11.grid(row=2, column=12, rowspan=25)
l12 = Label(windows, text='Start :')
l12.grid(row=7, column=1)
l12 = Label(windows, text='Stop :')
l12.grid(row=7, column=3)
l13 = Label(windows, text='R :')
l13.grid(row=13, column=3)
l14 = Label(windows, text='φ Pole :')
l14.grid(row=15, column=3)
l15 = Label(windows, text=' ')
l15.grid(row=31, column=9)

# DEFINISI INPUT TEXT STRING
e1 = Entry(windows, width=8)
e1.grid(row=2, column=3)
e2 = Entry(windows, width=8)
e2.grid(row=25, column=2)
e3 = Entry(windows, width=8)
e3.grid(row=26, column=2)
e4 = Entry(windows, width=8)
e4.grid(row=25, column=5)
e5 = Entry(windows, width=8)
e5.grid(row=26, column=5)

# DEFINISI INPUT BUTTON
b1 = Button(windows, text='INPUT', command=awal)
b1.grid(row=2, column=5)
b2 = Button(windows, text='PLOT\nDFT', command=Windowing)
b2.grid(row=9, column=3, rowspan=2)
b3 = Button(windows, text='SIMULATE', command=Simulation)
b3.grid(row=23, column=4, columnspan=2)
b4 = Button(windows, text='GENERATE', command=Generate)
b4.grid(row=2, column=9)
b5 = Button(windows, text='RESULT', command=Result_Show)
b5.grid(row=23, column=1, columnspan=2)

# SPINBOX
spin1 = Spinbox(windows, from_=0, to=None, width=5, command=Hanning)
spin1.grid(row=7, column=2)
spin2 = Spinbox(windows, from_=0, to=None, width=5, command=Hanning)
spin2.grid(row=7, column=4)
spin3 = Spinbox(windows, from_=0, to=1, width=5, format="%.2f", increment=0.01, command=pole_zero)
spin3.grid(row=14, column=3)
spin4 = Spinbox(windows, from_=0, to=360, width=5, command=pole_zero)
spin4.grid(row=16, column=3)

windows.mainloop()
