import sympy as sy
import numpy as ny
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fungsi_polinomial(x,a,b,c):
    return a*x+b

def gambardata(titik, baris):
    i=0
    sigmax=0
    sigmay=0
    sigmaxkuadrat=0
    sigmaxy=0
    titikx=[]
    titiky=[]

    for i in range (0, baris):
        sigmax = sigmax+titik[i][0]
        sigmay = sigmay+titik[i][1]
        sigmaxkuadrat = sigmaxkuadrat+titik[i][0]**2
        sigmaxy = sigmaxy+titik[i][0]*titik[i][1]
        titikx.insert(i, titik[i][0])
        titiky.insert(i, titik[i][1])
    bawah = min(titik)
    atas = max(titik)
    kuadratsigmax = sigmax**2

    a=(sigmay*sigmaxkuadrat-sigmax*sigmaxy)/(baris*sigmaxkuadrat-kuadratsigmax)
    b=(baris*sigmaxy-sigmax*sigmay)/(baris*sigmaxkuadrat-kuadratsigmax)

    x = sy.Symbol('x')
    f=a+b*x
    horizontal = ny.linspace(bawah[0], atas[0], 400)
    fungsi = sy.lambdify(x, f, "numpy")

    popt, pcov = curve_fit(fungsi_polinomial, titikx, titiky)
    plt.plot(horizontal, fungsi_polinomial(horizontal, *popt))

    for i in range (0, baris):
        plt.plot(titik[i][0], titik[i][1], 'bo')
    plt.plot(horizontal, fungsi(horizontal))
    plt.show()
    return


def barisdata(namafile):
    text = open(namafile, 'r')
    text.seek(0)
    baris = sum(1 for line in text)
    return baris


def ambildata(namafile, baris):
    text = open(namafile, 'r')
    text.seek(0)
    i=0
    data =[]
    line=text.readline()
    while line:
        data.insert(i, line)
        data[i] = data[i].replace('\n','')
        data[i] = data[i].split(',')
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
        i += 1
        line = text.readline()
    return data



namafile = 'data.txt'
gambardata(ambildata(namafile, barisdata(namafile)), barisdata(namafile))
