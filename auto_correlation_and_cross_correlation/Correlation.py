import matplotlib.pyplot as plt
from numpy import arange, zeros, array


def autocorrelation(
        inputArray):
    """

    :rtype: Array of Object by AutoCorrelation
    """

    totalData = len(inputArray)
    xValue = arange(totalData)
    yResult = zeros(totalData)

    for iteration in xValue:
        yResult[iteration] = sum(inputArray[0:totalData-iteration] * inputArray[iteration:totalData] / totalData)

    return yResult

def crosscorrelation(
        input1Array,
        input2Array):
    """

    :rtype: Array of Object by AutoCorrelation
    """

    totalData = len(input1Array)
    xValue = arange(totalData)
    yResult = zeros(totalData)

    for iteration in xValue:
        yResult[iteration] = sum(input1Array[0:totalData-iteration] * input2Array[iteration:totalData] / totalData)

    return yResult


if __name__ == "__main__":
    heelDataFile = open("Data/Heel123.txt", "r")
    heelArray = []
    for heelData in heelDataFile.readlines():
        heelArray.append(float(heelData.replace("\n", "")))
    heelDataFile.close()
    heelArray = array(heelArray)

    toeDataFile = open("Data/Toe123.txt", "r")
    toeArray = []
    for toeData in toeDataFile.readlines():
        toeArray.append(float(toeData.replace("\n", "")))
    toeDataFile.close()
    toeArray = array(toeArray)

    plt.figure(0)
    plt.plot(autocorrelation(heelArray), label="Heel")
    plt.plot(autocorrelation(toeArray), label="Toe")
    plt.xlabel("Sequence")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.figure(1)
    plt.plot(crosscorrelation(heelArray, toeArray), label="Heel to Toe Correlation")
    plt.plot(crosscorrelation(toeArray, heelArray), label="Toe to Heel Correlation")
    plt.xlabel("Sequence")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.figure(2)
    plt.plot(heelArray, label="Heel")
    plt.plot(toeArray, label="Toe")
    plt.xlabel("Sequence")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()
