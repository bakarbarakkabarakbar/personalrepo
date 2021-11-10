import numpy as ny

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

a = [[1,0],[0,1]]
b = [[1,0],[0,1]]

print(Pertambahan(a,b))