import matplotlib.pyplot as plt
from numpy import sin, zeros, arange, exp, pi
from scipy import ifft


def sinusequations(
        x,
        y):
    return sin(x)


def rungekutta4thorder(equations,
                       xValue,
                       yStart):
    """

    :rtype: Array of Object by Runge Kutta 4th Order
    """
    totalData = len(xValue)
    height = xValue[1] - xValue[0]
    yResult = zeros(totalData)
    yResult[0] = yStart

    for iteration in arange(totalData - 1):
        k1 = height * equations(xValue[iteration], yResult[iteration])
        k2 = height * equations(xValue[iteration] + 0.5 * height, yResult[iteration])
        k3 = height * equations(xValue[iteration] + 0.5 * height, yResult[iteration])
        k4 = height * equations(xValue[iteration] + height, yResult[iteration])
        yResult[iteration + 1] += yResult[iteration] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return yResult


def inversediscretefouriertransfrom(
        inputArray):
    """

    :rtype: Array of Object by IDFT
    """

    totalData = len(inputArray)
    xValue = arange(totalData)
    yResult = zeros(totalData)

    for iterationOne in xValue:
        yResult[iterationOne] = sum(inputArray * exp(2j
                                                     * pi
                                                     * iterationOne
                                                     * xValue
                                                     / totalData) / totalData)

    return abs(yResult)


if __name__ == "__main__":
    xStart = 0
    xEnd = 100
    yStart = 0
    height = 0.1
    totalData = int((xEnd - xStart) / height)
    xValue = arange(xStart, xEnd, height)

    yResultRungeKutta = rungekutta4thorder(sinusequations, xValue, yStart)
    yResultIDFT = inversediscretefouriertransfrom(sinusequations(xValue, zeros(totalData)))

    plt.figure(1)
    plt.plot(xValue, yResultRungeKutta)
    plt.figure(2)
    plt.plot(xValue, yResultIDFT)

    plt.show()