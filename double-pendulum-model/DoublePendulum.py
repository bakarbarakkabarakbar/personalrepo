import numpy as ny
from math import sin, cos, radians
import matplotlib.pyplot as plt
from time import sleep

def Invers(Matrix):
    n = len(Matrix)
    MatrixIdentitas = ny.zeros((n, n))

    for i in range(0, n):
        MatrixIdentitas[i][i] = 1

    for i in range(0, n):
        Pembagi = Matrix[i][i]
        for j in range(0, n):
            MatrixIdentitas[i][j] = MatrixIdentitas[i][j] / Pembagi
            Matrix[i][j] = Matrix[i][j] / Pembagi

        for k in range (0, n):
            if k == i:
                continue
            Pembagi = Matrix[k][i]
            for l in range (0, n):
                MatrixIdentitas[k][l] = MatrixIdentitas[k][l] - MatrixIdentitas[i][l] * Pembagi
                Matrix[k][l] = Matrix[k][l] - Matrix[i][l] * Pembagi
    return MatrixIdentitas

def Perkalian(matrixA, matrixB):
    ordomatrixA = [len(matrixA), len(matrixA[0])]
    ordomatrixB = [len(matrixB), len(matrixB[0])]
    if ordomatrixA[1] == ordomatrixB[0]:
        hasil = ny.zeros((ordomatrixA[0], ordomatrixB[1]))
        n1 = ordomatrixA[0]
        n2 = ordomatrixB[1]
        n3 = ordomatrixA[1]
        for i in range (0, n1):
            for j in range (0, n2):
                for k in range (0, n3):
                    hasil[i][j] = hasil[i][j] + matrixA[i][k] * matrixB[k][j]
        return hasil
    else:
        print('Error Perkalian')

def Pertambahan(matrixA, matrixB):
    ordomatrixA = [len(matrixA), len(matrixA[0])]
    ordomatrixB = [len(matrixB), len(matrixB[0])]
    if ordomatrixA == ordomatrixB:
        hasil = ny.zeros((ordomatrixA[0], ordomatrixA[1]))
        n1 = ordomatrixA[0]
        n2 = ordomatrixB[1]
        for i in range (0, n1):
            for j in range (0, n2):
                hasil[i][j] = matrixA[i][j] + matrixB[i][j]
        return hasil
    else:
        print('Error Pertambahan')

def Pengurangan(matrixA, matrixB):
    ordomatrixA = [len(matrixA), len(matrixA[0])]
    ordomatrixB = [len(matrixB), len(matrixB[0])]
    if ordomatrixA == ordomatrixB:
        hasil = ny.zeros((ordomatrixA[0], ordomatrixA[1]))
        n1 = ordomatrixA[0]
        n2 = ordomatrixB[1]
        for i in range (0, n1):
            for j in range (0, n2):
                hasil[i][j] = matrixA[i][j] - matrixB[i][j]
        return hasil
    else:
        print('Error Pengurangan')

def fungsiTetadotdot(t, teta1, teta2, tetadot1, tetadot2):
    m11 = (1/4*m1 + m2)*l1**2 + i1
    m12 = 1/2*m2*l1*l2*cos(teta1 - teta2)
    m21 = 1/2*m2*l1*l2*cos(teta1 - teta2)
    m22 = 1/4*m2*l2**2 + i2

    m = ny.zeros((2,2))
    m = [[m11, m12], [m21, m22]]

    tau = ny.zeros((2,1))

    c11 = 1/2*m2*l1*l2*sin(teta1 - teta2)*tetadot2
    c12 = -1/2*m2*l1*l2*sin(teta1 - teta2)*(tetadot1 - tetadot2)
    c21 = -1/2*m2*l1*l2*sin(teta1 - teta2)*(tetadot1 - tetadot2)
    c22 = -1/2*m2*l1*l2*tetadot1*sin(teta1 - teta2)

    c = ny.zeros((2,2))
    c = [[c11, c12], [c21, c22]]

    tetadot = ny.zeros((2,1))
    tetadot[0] = tetadot1
    tetadot[1] = tetadot2

    g11 = (1/2*m1 + m2)*graf*l1*sin(teta1)
    g21 = 1/2*m2*graf*l2*sin(teta2)
    g = ny.zeros((2,1))
    g = [[g11], [g21]]
    return Pengurangan(Pengurangan(Perkalian(Invers(m), tau), Perkalian(Perkalian(Invers(m), c), tetadot)), Perkalian(Invers(m), g))

def rungeKutta(t, teta1, teta2, tetadot1, tetadot2):
    k1 = ny.zeros((2,1))
    k2 = ny.zeros((2,1))
    k3 = ny.zeros((2,1))
    k4 = ny.zeros((2,1))

    tetadotdot = fungsiTetadotdot(t, teta1, teta2, tetadot1, tetadot2)
    k1[0] = dt/2*tetadotdot[0]
    k1[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt/2, teta1 + dt/2*(tetadot1 + k1[0]/2), teta2 + dt/2*(tetadot2 + k1[1]/2), tetadot1 + k1[0], tetadot2 + k1[1])
    k2[0] = dt/2*tetadotdot[0]
    k2[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt/2, teta1 + dt/2*(tetadot1 + k1[0]/2), teta2 + dt/2*(tetadot2 + k1[1]/2), tetadot1 + k2[0], tetadot2 + k2[1])
    k3[0] = dt/2*tetadotdot[0]
    k3[1] = dt/2*tetadotdot[1]

    tetadotdot = fungsiTetadotdot(t + dt, teta1 + dt*(tetadot1 + k3[0]), teta2 + dt*(tetadot2 + k3[1]), tetadot1 + 2*k3[0], tetadot2 + 2*k3[1])
    k4[0] = dt/2*tetadotdot[0]
    k4[1] = dt/2*tetadotdot[1]

    teta1baru = teta1 + dt*(tetadot1 + ((k1[0] + k2[0] + k3[0])/3))
    teta2baru = teta2 + dt*(tetadot2 + ((k1[1] + k2[1] + k3[1])/3))

    tetadot1baru = tetadot1 + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/3
    tetadot2baru = tetadot2 + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/3

    return teta1baru, teta2baru, tetadot1baru, tetadot2baru

m1 = 1
m2 = 1
l1 = 1
l2 = 1
teta1 = radians(90)
teta2 = radians(90)
dt = 0.02
interval = 0.2
graf = 9.8
tetadot1 = radians(0)
tetadot2 = radians(0)

i1 = m1*l1
i2 = m2*l2

fig = plt.figure()
i=1

def gambarGaris(teta1, teta2, x1,y1, x2, y2, titikx1, titiky1, titikx2, titiky2):
    x0 = 0
    y0 = 0
    garis1x, garis1y = [x0, x1], [y0, y1]
    garis2x, garis2y = [x1, x2], [y1, y2]

    ax = fig.add_subplot(224)
    plt.plot(dt*i, teta1*180, '_')
    plt.xlabel('waktu')
    plt.ylabel('teta1')
    ax = fig.add_subplot(223)
    plt.plot(dt * i, teta2 * 180, '_')
    plt.xlabel('waktu')
    plt.ylabel('teta2')
    ay = fig.add_subplot(211)
    plt.xlim(-3,3)
    plt.ylim(-3,0)
    plt.scatter(titikx1, titiky1)
    plt.scatter(titikx2, titiky2)
    plt.plot(garis1x, garis1y, marker='o')
    plt.plot(garis2x, garis2y, marker='o')
    plt.pause(dt)
    ay.cla()

while(True):
    x1 = l1 * sin(teta1)
    y1 = -l1 * cos(teta1)
    x2 = x1 + l2 * sin(teta2)
    y2 = y1 - l2 * cos(teta2)
    px1 = 1 / 2 * x1
    py1 = 1 / 2 * y1
    px2 = x1 + 1 / 2 * l2 * sin(teta2)
    py2 = y1 - 1 / 2 * l2 * cos(teta2)

    gambarGaris(teta1, teta2, x1, y1, x2, y2, px1, py1, px2, py2)
    i = i + 1
    hasil = rungeKutta(dt, teta1, teta2, tetadot1, tetadot2)
    teta1 = hasil[0]
    teta2 = hasil[1]
    tetadot1 = hasil[2]
    tetadot2 = hasil[3]