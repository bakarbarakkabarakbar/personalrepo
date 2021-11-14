from numpy import sin
import matplotlib.pyplot as plt


def fastfouriertransform(
        inputArray):
    inputLength = len(inputArray)
    def reversenumber