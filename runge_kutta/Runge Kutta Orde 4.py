import matplotlib.pyplot as plt
import numpy as np

def dydx(x):
    return 2*x

def rungeKutta(
        xdot, 
        y0, 
        h):
    k1 = h * dydx(xdot)
    k2 = h * dydx(xdot + 0.5*h)
    k3 = h * dydx(xdot + 0.5*h)
    k4 = h * dydx(xdot + h)
    y = y0 + (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    return y

x0 = 0
y = 0
h = 0.02

xvalue=[]
yvalue=[]

xvalue.append(x0)

for i in range(0, 1000):
    yvalue.append(
            rungeKutta(
                x0, 
                yvalue[i], 
                h)
            )
    xvalue.append(x0)
    x0 +=  h

print(xvalue, yvalue)

plt.plot(xvalue, yvalue)
plt.show()
