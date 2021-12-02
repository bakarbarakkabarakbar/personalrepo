import numpy
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter import *


def bukafile():
    Tk().withdraw()
    namafile = askopenfilename()
    if namafile == '':
        showerror(title='File Open Error', message="Error dalam membuka file, coba lagi")
        exit()

    bukafile = open(namafile, 'r')
    data = bukafile.readlines()

    print(data)
    data[0] = data[0].replace('\n', '')
    jumlahdata = int(data[0])
    for a in range(1, jumlahdata):
        data[a] = data[a].replace('\n','')
        data[a][0] = data[a][0].replace(' ', '')
        data[a][0] = float(data[a][0])
        data[a][1] = float(data[a][1])
        data[a][2] = float(data[a][2])
        #data[a] = data[a].split('\t')


    print(data)

windows = Tk()
bukafilebutton = Button(windows, text='Open File', command=bukafile).grid(row=0, column=0)
windows.mainloop()
