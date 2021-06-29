import sympy as sy
import numpy as ny

Matrix = [[5, 1, 2], [3, 4, 2], [2, 1, 6]]

def printMatrix(Matrix):
    for i in range (0, n):
        print(Matrix[i])

def Invers(Matrix):
    n = len(Matrix)

    MatrixIdentitas = ny.zeros((n, n))

    for i in range(0, n):
        MatrixIdentitas[i][i] = 1

    ##Metode Gauss Jordan

    ## Pivoting matrix
    for i in range(0, n):
        Pembagi = Matrix[i][i]
        for j in range(0, n):
            MatrixIdentitas[i][j] = MatrixIdentitas[i][j] / Pembagi
            Matrix[i][j] = Matrix[i][j] / Pembagi

        ## Dividing Row
        for k in range (0, n):
            if k == i:
                continue
            Pembagi = Matrix[k][i]
            for l in range (0, n):
                MatrixIdentitas[k][l] = MatrixIdentitas[k][l] - MatrixIdentitas[i][l] * Pembagi
                Matrix[k][l] = Matrix[k][l] - Matrix[i][l] * Pembagi
    return MatrixIdentitas


print('Input Matrix yaitu :')
printMatrix(Matrix)
print('Invers Matrixnya : ')
printMatrix(Invers(Matrix))