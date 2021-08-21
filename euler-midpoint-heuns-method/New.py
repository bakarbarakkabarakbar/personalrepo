import numpy as ny
import matplotlib.pyplot as plt

y0=1
h=0.5
xBawah=0
xAtas=4

titik=[]
titikx=[]
titiky=[]
n=0
yEuler=0
yHeuns=0
yMidpoint=0
yRungeKuttaOrde3=0
yRungeKuttaOrde4=0
k1=0
k2=0
k3=0
k4=0
ySetengah=0
yPrediktor=0
yKorektor=0
k=1

def dyperdx(x,y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def fungsi(x):
    return -1/2*x**4 +4*x**3 -10*x**2 + 8.5*x + 1

horizontal = ny.linspace(xBawah, xAtas, 400)
plt.plot(horizontal, fungsi(horizontal), label='True Value')

def Euler(yEuler,h,xBawah,xAtas):
    del titik[:]
    n = (xAtas-xBawah)/h
    n = int(n)
    for i in range (0,n+1):
        titik.append([xBawah + h * i, yEuler])
        yEuler=yEuler+h*dyperdx(xBawah+h*i,yEuler)
    gambar(titik, 'Euler')

def Midpoint(yMidpoint,h,xBawah,xAtas):
    del titik[:]
    n = (xAtas - xBawah) / h
    n = int(n)
    for i in range (0,n+1):
        titik.append([xBawah + h * i, yMidpoint])
        ySetengah=yMidpoint+h/2*dyperdx(xBawah+h*i,yMidpoint)
        yMidpoint=yMidpoint+h*dyperdx(xBawah+h/2+h*i,ySetengah)
    gambar(titik, 'Midpoint')

def Heuns(yHeuns,h,xBawah,xAtas):
    del titik[:]
    n = (xAtas - xBawah) / h
    n = int(n)
    for i in range (0, n+1):
        titik.append(([xBawah + h * i, yHeuns]))
        yPrediktor = yHeuns + h * dyperdx(xBawah + h * i, yHeuns)
        for j in range (0, k):
            yKorektor= yHeuns + (dyperdx(xBawah+h*i,yHeuns)+dyperdx(xBawah+h*(i+1),yPrediktor))/2*h
            yPrediktor=yKorektor
        yHeuns=yKorektor
    gambar(titik, 'Heuns')

def RungeKuttaOrde3(yRungeKuttaOrde3,h,xBawah,xAtas):
    del titik[:]
    n = (xAtas - xBawah) / h
    n = int(n)
    for i in range (0, n+1):
        titik.append([xBawah + h * i, yRungeKuttaOrde3])
        k1 = h*dyperdx(xBawah + h * i, yRungeKuttaOrde3)
        k2 = h*dyperdx(xBawah + h/2 + h*i, yRungeKuttaOrde3 + 1/2*k1*h)
        k3 = h*dyperdx(xBawah + h +h*i, yRungeKuttaOrde3 - k1*h + 2*k2*h)
        yRungeKuttaOrde3 = yRungeKuttaOrde3 + 1/6*(k1 + 4*k2 + k3)
    gambar(titik, 'RungeKuttaOrde3')

def RungeKuttaOrde4(yRungeKuttaOrde4,h,xBawah,xAtas):
    del titik[:]
    n = (xAtas - xBawah) / h
    n = int(n)
    for i in range (0, n+1):
        titik.append([xBawah + h * i, yRungeKuttaOrde4])
        k1 = h*dyperdx(xBawah + h*i, yRungeKuttaOrde4)
        k2 = h*dyperdx(xBawah + h/2 + h*i, yRungeKuttaOrde4 + k1/2)
        k3 = h*dyperdx(xBawah + h/2 + h*i, yRungeKuttaOrde4 + k2/2)
        k4 = h*dyperdx(xBawah + h + h*i, yRungeKuttaOrde4 + k3)
        yRungeKuttaOrde4 = yRungeKuttaOrde4 + 1/6*(k1+2*k2+2*k3+k4)
    gambar(titik, 'RungeKuttaOrde4')


def gambar(titik, method):
    n = (xAtas-xBawah)/h
    n = int(n)
    for i in range(0, n+1):
        titikx.append(titik[i][0])
        titiky.append(titik[i][1])
    if method == 'Euler':
        plt.plot(titikx, titiky, label=method, color='green')
    elif method == 'Heuns':
        plt.plot(titikx, titiky, label=method, color='blue')
    elif method == 'Midpoint':
        plt.plot(titikx, titiky, label=method, color='red')
    elif method == 'RungeKuttaOrde3':
        plt.plot(titikx, titiky, label=method, color='yellow')
    elif method == 'RungeKuttaOrde4':
        plt.plot(titikx, titiky, label=method, color='purple')
    del titikx[:]
    del titiky[:]

Euler(y0,h,xBawah,xAtas)
Midpoint(y0,h,xBawah,xAtas)
Heuns(y0,h,xBawah,xAtas)
RungeKuttaOrde4(y0,h,xBawah,xAtas)
RungeKuttaOrde3(y0,h,xBawah,xAtas)
plt.legend()
plt.show()