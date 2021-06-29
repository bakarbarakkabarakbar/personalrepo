import sympy as sy
import numpy as ny
import matplotlib.pyplot as plt

yEuler=[0.0]
yMidpoint=[1.0]
yHeuns=[1.0]
yKorektor=[1.0]
k=1
xlow=0
xhigh=4
h=0.5

def dyperdx(x,y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def fungsi(x):
    return -1/2*x**4 +4*x**3 -10*x**2 + 8.5*x + 1

def Euler(yEuler,h,xlow,xhigh):
    for i in range(0, 8):
        yEuler.append(yEuler[i]+h*dyperdx(xlow+h*i,yEuler[i]))
    x=[0,0.5,1,1.5,2,2.5,3,3.5,4]
    print(x,yEuler)
    plt.plot(x, yEuler, label='Euler Method', color='green')
    return

def MidPoint(yMidpoint,h,xlow,xhigh):
    for i in range(0, round((xhigh-xlow)/h)):
        ysetengah = yMidpoint[i]+h/2*dyperdx(xlow+h/2*i,yMidpoint[i])
        yMidpoint.append(yMidpoint[i]+h*dyperdx(xlow+h/2*i,ysetengah))
        plt.plot(xlow+h*i, yMidpoint[i], label='Midpoint Method', color='blue')
        print('b')
    return

def Heuns(yHeuns,h,xlow,xhigh):
    for i in range(0, round((xhigh-xlow)/h)):
        yKorektor.append(yHeuns[i] + h*dyperdx(xlow + h*i,yHeuns[i]))
        for j in range(0,k):
            yKorektor.append(yHeuns[i]+h*(dyperdx(xlow+h*i,yHeuns[i])+dyperdx(xlow+h*i+1,yKorektor[j]))/2)
        yHeuns.append(yKorektor[k])
        del yKorektor[:]
        plt.plot(xlow+h*i, yHeuns[i], label='Heuns Method', color='red')
    return

horizontal = ny.linspace(xlow, xhigh, 400)
plt.plot(horizontal, fungsi(horizontal))
Euler(yEuler,h,xlow,xhigh)
MidPoint(yMidpoint,h,xlow,xhigh)
Heuns(yHeuns,h,xlow,xhigh)
plt.show()
