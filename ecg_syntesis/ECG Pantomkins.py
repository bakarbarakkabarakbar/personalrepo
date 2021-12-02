import numpy
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter

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
        tipe_data1 = data[a][1]
        tipe_data2 = data[a][2]
        continue
    if a == 1:
        sample_interval = float(data[a][0].replace('sec', ''))
        satuan_data1 = data[a][1]
        satuan_data2 = data[a][2]
        continue
    data[a][0] = int(data[a][0])
    data[a][1] = float(data[a][1])
    data[a][2] = float(data[a][2])

data = numpy.array(data)
data0 = numpy.array(data[:, 0])
data1 = numpy.array(data[:, 1])
data2 = numpy.array(data[:, 2])

print(data0)
print(data1)
print(data2)

# Mendapatkan Frekuensi Sampling
periodesampling = sample_interval
frekuensisampling = round(1/periodesampling)

# Menghilangkan Header yang tidak dibutuhkan

data0 = numpy.delete(data0,0)
data0 = numpy.delete(data0,0)
data1 = numpy.delete(data1,0)
data1 = numpy.delete(data1,0)
data2 = numpy.delete(data2,0)
data2 = numpy.delete(data2,0)

def plotfigure():
    plt.figure(figsize=(12, 2))
    x = var.get()
    if x == 1:
        plt.plot(data1, linewidth=0.5)
    if x == 2:
        plt.plot(data2, linewidth=0.5)
    plt.show()

root = tkinter.Tk()
var = tkinter.IntVar()
tkinter.Label(master=root, text="""Tampilkan data berdasarkan database yang dipilih:""", justify = tkinter.CENTER, padx = 20).pack()
# tkinter.Button(master=root, text='ECG2', command=plotfigure2).pack()
radio_uno = tkinter.Radiobutton(master=root, text=tipe_data1, value=1, variable=var, command=plotfigure)
radio_due = tkinter.Radiobutton(master=root, text=tipe_data2, variable=var, value=2)
button_uno = tkinter.Button(master=root, text='Pilih Data', command=plotfigure)

radio_uno.pack()
radio_due.pack()
button_uno.pack()

tkinter.mainloop()

