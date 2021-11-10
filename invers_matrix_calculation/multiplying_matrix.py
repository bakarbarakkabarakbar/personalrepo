import numpy as ny

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

a = [[2,0],[0,2]]
b = [[1,0,2],[0,1,1]]

print(Perkalian(a,b))
