import tkinter
import math as mt
import numpy as np
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler


# DEKLARASI VARIABLE TAMBAHAN
N, n, y= None, None, None
manual = np.array([1,2,9,-2,3,-1,10])
font9 = "-family {Showcard Gothic} -size 14 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"

# FUNGSI PROGRAM
windows = tkinter.Tk()

l1 = tkinter.Label(windows, text='Linear Prediction', font=font9)
l1.pack(fill= tkinter.X, side=tkinter.TOP)

def input_out():
    rep = askopenfilename(parent=windows)
    print(rep)
    global N, n, y

    f = open(rep, "r")
    input = f.readlines()
    N = np.size(input)
    n = np.zeros([N])
    y = np.zeros([N])

    inisial = 0
    for a in input:
        aa = a.replace('\n', '')
        aaa = aa.split('\t')
        n[inisial] = float(aaa[0])
        y[inisial] = float(aaa[1])
        inisial += 1

    grafik1.clear()
    grafik1.add_subplot(111).plot(n, y)
    grafik1_windows.draw()
    entry1.delete(0, tkinter.END)
    entry1.insert(0, N)
    spin1.delete(0, tkinter.END)
    spin1._setitem('from', 0)
    spin1._setitem_('to', N-1)

def input_in():
    global N, n, y

    N = np.size(manual)
    n = np.zeros([N])
    y = np.zeros([N])

    inisial = 0
    for a in manual:
        n[inisial] = inisial
        y[inisial] = a
        inisial += 1

    grafik1.clear()
    grafik1.add_subplot(111).plot(n, y)
    grafik1_windows.draw()
    entry1.delete(0, tkinter.END)
    entry1.insert(0, N)
    spin1.delete(0, tkinter.END)
    spin1._setitem('from', 0)
    spin1._setitem_('to', N-1)

def Sinus():
    global N, n, y

    N = 1000
    n = np.zeros([N])
    y = np.zeros([N])

    inisial = 0
    for i in range(N):
        n[inisial] = inisial
        y[inisial] = mt.sin(2*np.pi*i*10/N)
        inisial += 1

    grafik1.clear()
    grafik1.add_subplot(111).plot(n, y)
    grafik1_windows.draw()
    entry1.delete(0, tkinter.END)
    entry1.insert(0, N)
    spin1.delete(0, tkinter.END)
    spin1._setitem('from', 0)
    spin1._setitem_('to', N-1)


def Generate():
    global a, p, rxx

    p = int(spin1.get())
    rxx = AutoCor(y, p, N)
    a = koef(rxx, p, N)
    predict(a, p, y, N)
    freq_resp(a, p)


def AutoCor(data1, p1, N1):
    y = np.zeros(np.size(data1))
    for i in range(N1):
        for j in range(N1 - i):
            b = data1[j] * data1[i + j]
            y[i] += (b / N1)
    return y


def koef(data1, p1, N1):
    global Rxx, a0
    Rxx = np.zeros((p1, p1))
    for i in range(p1):
        for j in range(p1):
            if i == j:
                Rxx[i][j] = data1[0]
            elif i < j:
                Rxx[i][j] = data1[j - i]
            elif i > j:
                Rxx[i][j] = data1[i - j]

    Rxx_inv = np.linalg.inv(Rxx)
    # rxx vector
    rxx_vct = rxx[1:p1 + 1]  # mengabaikan rxx[0]
    rxx_vct = np.asarray(rxx_vct)  # rxx jadi array
    np.reshape(rxx_vct, (np.size(rxx_vct), 1))
    # perkalian matriks
    a0 = np.dot(Rxx_inv, rxx_vct)

    print(a0)

    return a0.transpose()


def predict(a, p1, data1, N1):
    x_vct = np.zeros(N1)
    em = np.zeros(N1)
    eror = np.zeros(N1)
    for i in range(N1):
        for j in range(p1):
            em[i] += a[j] * data1[i - j]
        em[i] = data1[i] - em[i]

    for i in range(N1):
        for j in range(1, p1):
            x_vct[i] += a[j] * data1[i - j]
        x_vct[i] += em[i]
        eror[i] = data1[i] - x_vct[i]

    x1 = np.arange(np.size(em))
    grafik2.clear()
    grafik2.add_subplot(111).plot(x1, em)
    grafik2_windows.draw()

    x2 = np.arange(np.size(x_vct))
    grafik3.clear()
    grafik3.add_subplot(111).plot(x2, x_vct + eror)
    grafik3_windows.draw()


def freq_resp(a, p1):
    q = 0
    Ax = []
    hx = []
    while q <= (31.4 + 1):
        re_x = 0
        im_x = 0
        for i in range(p1):
            re_x += a[i] * mt.cos(i * q)
            im_x += a[i] * mt.sin(i * q)
        Ax += [mt.sqrt(((1 - re_x) * 2) + (im_x) * 2)]
        q += 1
    q = 0
    while q < (31.4 + 1):
        hx += [int(1 / float(Ax[q]))]
        q += 1
    q = np.arange(np.size(Ax))

    axz.clear()
    axz.plot(q, Ax, color = 'r')
    axz.plot(q, hx, color = 'y')
    grafik4_windows.draw()

    # q = 0
    # while q <= 3.14:
    #     rex = 0
    #     imx = 0
    #     for i in range(p):
    #         rex += a[i] * mt.cos(i * q)
    #         imx += a[i] * mt.sin(i * q)
    #     ax = mt.sqrt(mt.pow(1 - rex, 2) + mt.pow(imx,2))
    #     hx = 1 / ax
    #     q = q + 0.1
# data1_t = data1.transpose()
    # m_1 = []
    # sgm_r = np.zeros(N1)
    # sgm_i = np.zeros(N1)
    # sgm = []
    # Hf = []
    # for i in range(p1):
    #     m_1 += [a0[i] * data1[i]]
    # for i in range(N1):
    #     for j in range(p1):
    #         sgm_r[i] += (a0[j] * cos(2 * pi * j * i))
    #         sgm_i[i] += (a0[j] * sin(-2 * pi * j * i))
    # for i in range(N1):
    #     sgm += [sqrt((sgm_r[i] * 2) + (sgm_i[i] * 2))]
    #
    # m_21 = matmul(a, Rxx)
    # m_2 = matmul(m_21, a0)
    # G = power((data1[0] - 2 * m_1 + m_2), 0.5)
    #
    # for i in range(N1):
    #     Hf += [G / (1 - sgm[i])]
    # xHf = np.arange(np.size(Hf))
    # fig4.clear()
    # ax4 = fig4.add_subplot(111)
    # ax4.plot(xHf, Hf[0], linewidth=0.5)
    # ax4.set_title('Sinyal Hasil konstruksi', fontsize=6)
    # ax4.set_ylabel('amplitudo', fontsize=6)
    # ax4.tick_params(direction='in', labelsize=6)
    # plt3_windows.draw()


# MEMASANG ATRIBUT PADA WINDOWS
frame1 = tkinter.Frame(master=windows)
frame1.pack(fill=tkinter.X)
frame11 = tkinter.Frame(frame1)
frame11.pack(padx=5, side=tkinter.LEFT)
frame12 = tkinter.Frame(frame1)
frame12.pack(padx=5, side=tkinter.LEFT)
grafik1 = Figure(figsize=(5,1.5))
grafik2 = Figure(figsize=(5,1.5))
grafik1_windows = FigureCanvasTkAgg(grafik1, frame11)
grafik2_windows = FigureCanvasTkAgg(grafik2, frame12)
toolbar1 = NavigationToolbar2Tk(grafik1_windows, frame11)
toolbar1.update()
toolbar2 = NavigationToolbar2Tk(grafik2_windows, frame12)
toolbar2.update()
grafik1_windows.get_tk_widget().pack(side=tkinter.TOP)
grafik2_windows.get_tk_widget().pack(side=tkinter.TOP)

frame2 = tkinter.Frame(master=windows)
frame2.pack(fill=tkinter.X)
frame21 = tkinter.Frame(frame2)
frame21.pack(padx=5, side=tkinter.LEFT)
frame22 = tkinter.Frame(frame2)
frame22.pack(padx=5, side=tkinter.LEFT)
grafik3 = Figure(figsize=(5,1.5))
grafik4 = Figure(figsize=(5,1.5))
grafik3_windows = FigureCanvasTkAgg(grafik3, frame21)
grafik4_windows = FigureCanvasTkAgg(grafik4, frame22)
toolbar3 = NavigationToolbar2Tk(grafik3_windows, frame21)
toolbar3.update()
toolbar4 = NavigationToolbar2Tk(grafik4_windows, frame22)
toolbar4.update()
grafik3_windows.get_tk_widget().pack(side=tkinter.TOP)
grafik4_windows.get_tk_widget().pack(side=tkinter.TOP)

grafik1.add_subplot(111)
grafik1_windows.draw()
grafik2.add_subplot(111)
grafik2_windows.draw()
grafik3.add_subplot(111)
grafik3_windows.draw()
axz = grafik4.add_subplot(111)
grafik4_windows.draw()

bantuan1 = tkinter.Frame(master=windows)
bantuan1.pack(fill=tkinter.X, side=tkinter.TOP, before=frame1)
frame_a1 = tkinter.Frame(bantuan1)
frame_a1.pack(padx=5, side=tkinter.LEFT)
label1 = tkinter.Label(frame_a1, text='n Data\t=')
label1.pack(side=tkinter.LEFT)
entry1 = tkinter.Entry(frame_a1, width=8)
entry1.pack(padx= 40, side=tkinter.LEFT)
#RADIO BUTTON
inputnya = tkinter.IntVar(frame_a1)
r0 = tkinter.Radiobutton(frame_a1, text='Open File', value=1, variable=inputnya, command=input_out)
r0.pack(padx= 20, side=tkinter.LEFT)
r1 = tkinter.Radiobutton(frame_a1, text='Sinus', value=2, variable=inputnya, command=Sinus)
r1.pack(padx= 20, side=tkinter.LEFT)
r2 = tkinter.Radiobutton(frame_a1, text='Manual', value=3, variable=inputnya, command=input_in)
r2.pack(side=tkinter.LEFT)

bantuan2 = tkinter.Frame(master=windows)
bantuan2.pack(fill=tkinter.X, side=tkinter.TOP, before=frame2)
frame_a2 = tkinter.Frame(bantuan2)
frame_a2.pack(padx=5, side=tkinter.LEFT)
spin1 = tkinter.Spinbox(frame_a2, from_=0, to=None, width=4, command=None)
spin1.pack(padx=50, side=tkinter.LEFT)
button1 = tkinter.Button(frame_a2, text='GENERATE', command=Generate)
button1.pack(padx=200, side=tkinter.LEFT)

def on_key_press_1(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, grafik1_windows, toolbar1)

def on_key_press_2(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, grafik2_windows, toolbar2)

def on_key_press_3(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, grafik3_windows, toolbar3)

def on_key_press_4(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, grafik4_windows, toolbar4)

grafik1_windows.mpl_connect("key_press_event", on_key_press_1)
grafik2_windows.mpl_connect("key_press_event", on_key_press_2)
grafik3_windows.mpl_connect("key_press_event", on_key_press_3)
grafik4_windows.mpl_connect("key_press_event", on_key_press_4)

windows.mainloop()