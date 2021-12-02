from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, \
    QSlider, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtWidgets
from pyqtgraph import PlotWidget
import sys
from numpy import arange, fft, linspace, pi, cos, sin, sqrt, array, log10, amax
from scipy.signal import TransferFunction, bode, butter, filtfilt, freqs
import control


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.resize(700, 700)
        self.setObjectName("Pengolahan Sinyal Biomedika")
        self.graphAnkle = PlotWidget(self)
        self.graphAnkle.setBackground(background='#2c302c')
        self.graphAnkle.setObjectName("graphAnkle")
        self.graphHeel = PlotWidget(self)
        self.graphHeel.setBackground(background='#2c302c')
        self.graphHeel.setObjectName("graphHeel")
        self.graphHip = PlotWidget(self)
        self.graphHip.setBackground(background='#2c302c')
        self.graphHip.setObjectName("graphHip")
        self.graphKnee = PlotWidget(self)
        self.graphKnee.setBackground(background='#2c302c')
        self.graphKnee.setObjectName("graphKnee")
        self.graphToe = PlotWidget(self)
        self.graphToe.setBackground(background='#2c302c')
        self.graphToe.setObjectName("graphToe")
        self.graphPoleZero = PlotWidget(self)
        self.graphPoleZero.setBackground(background=None)
        self.graphPoleZero.setObjectName("graphPoleZero")
        self.graphPoleZero.setXRange(-1, 1)
        self.graphPoleZero.setYRange(-1, 1)
        self.graphFrequencyResponse = PlotWidget(self)
        self.graphFrequencyResponse.setBackground(background=None)
        self.graphFrequencyResponse.setObjectName("graphFrequencyResponse")
        self.editAnkle = QLineEdit()
        self.editAnkle.setObjectName("editAnkle")
        self.editAnkle.setText("Ankle123.txt")
        self.labelAnkle = QLabel()
        self.labelAnkle.setText("0")
        self.editHeel = QLineEdit()
        self.editHeel.setObjectName("editHeel")
        self.editHeel.setText("Heel123.txt")
        self.labelHeel = QLabel()
        self.labelHeel.setText("0")
        self.editHip = QLineEdit()
        self.editHip.setObjectName("editHip")
        self.editHip.setText("Hip123.txt")
        self.labelHip = QLabel()
        self.labelHip.setText("0")
        self.editKnee = QLineEdit()
        self.editKnee.setObjectName("editKnee")
        self.editKnee.setText("Knee123.txt")
        self.labelKnee = QLabel()
        self.labelKnee.setText("0")
        self.editToe = QLineEdit()
        self.editToe.setObjectName("editToe")
        self.editToe.setText("Toe123.txt")
        self.labelToe = QLabel()
        self.labelToe.setText("0")
        self.buttonImport = QPushButton("Import", self)
        self.buttonImport.setObjectName("buttonImport")
        self.buttonImport.clicked.connect(self.importData)
        self.editLPF = QLineEdit()
        self.editLPF.setObjectName("editLPF")
        self.horizontalSliderLPF = QSlider()
        self.horizontalSliderLPF.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderLPF.setObjectName("horizontalSliderLPF")
        self.horizontalSliderLPF.setRange(1, 1000)
        self.horizontalSliderLPF.valueChanged.connect(self.updateLPF)
        self.horizontalSliderLPF.valueChanged.connect(self.lowPassFilter)
        self.horizontalSliderLPF.setSliderPosition(100)
        self.editHPF = QLineEdit()
        self.editHPF.setObjectName("editHPF")
        self.horizontalSliderHPF = QSlider()
        self.horizontalSliderHPF.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHPF.setObjectName("horizontalSliderHPF")
        self.horizontalSliderHPF.setRange(1, 1000)
        self.horizontalSliderHPF.valueChanged.connect(self.updateHPF)
        self.horizontalSliderHPF.valueChanged.connect(self.highPassFilter)
        self.horizontalSliderHPF.setSliderPosition(70)
        self.editBPF = QLineEdit()
        self.editBPF.setObjectName("editBPF")
        self.horizontalSliderBPF = QSlider()
        self.horizontalSliderBPF.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBPF.setObjectName("horizontalSliderBPF")
        self.horizontalSliderBPF.setRange(15, 1000)
        self.horizontalSliderBPF.valueChanged.connect(self.updateBPF)
        self.horizontalSliderBPF.valueChanged.connect(self.bandPassFilter)
        self.horizontalSliderBPF.setSliderPosition(250)
        self.editBSF = QLineEdit()
        self.editBSF.setObjectName("editBSF")
        self.horizontalSliderBSF = QSlider()
        self.horizontalSliderBSF.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBSF.setObjectName("horizontalSliderBSF")
        self.horizontalSliderBSF.setRange(15, 1000)
        self.horizontalSliderBSF.valueChanged.connect(self.updateBSF)
        self.horizontalSliderBSF.valueChanged.connect(self.bandStopFilter)
        self.horizontalSliderBSF.setSliderPosition(500)
        self.editPoleZeroRadius = QLineEdit()
        self.editPoleZeroRadius.setObjectName("editPoleZeroRadius")
        self.editPoleZeroTeta = QLineEdit()
        self.editPoleZeroTeta.setObjectName("editPoleZeroTeta")
        self.horizontalSliderPoleZeroRadius = QSlider()
        self.horizontalSliderPoleZeroRadius.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderPoleZeroRadius.setObjectName("horizontalSliderPoleZeroRadius")
        self.horizontalSliderPoleZeroRadius.setRange(1, 99)
        self.horizontalSliderPoleZeroRadius.valueChanged.connect(self.updatePoleZeroRadius)
        self.horizontalSliderPoleZeroRadius.setSliderPosition(1)
        self.horizontalSliderPoleZeroTeta = QSlider()
        self.horizontalSliderPoleZeroTeta.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderPoleZeroTeta.setObjectName("horizontalSliderPoleZeroTeta")
        self.horizontalSliderPoleZeroTeta.setRange(0, 179)
        self.horizontalSliderPoleZeroTeta.valueChanged.connect(self.updatePoleZeroTeta)
        self.horizontalSliderPoleZeroTeta.setSliderPosition(1)
        self.buttonFFT = QPushButton("FFT", self)
        self.buttonFFT.setObjectName("buttonFFT")
        self.buttonFFT.clicked.connect(self.FFTData)
        self.checkBoxAnkle = QCheckBox("Filter Ankle", self)
        self.checkBoxAnkle.setObjectName("checkBoxAnkle")
        self.checkBoxAnkle.stateChanged.connect(self.filterAnkle)
        self.checkBoxHeel = QCheckBox("Filter Heel", self)
        self.checkBoxHeel.setObjectName("checkBoxHeel")
        self.checkBoxHeel.stateChanged.connect(self.filterHeel)
        self.checkBoxHip = QCheckBox("Filter Hip", self)
        self.checkBoxHip.setObjectName("checkBoxHip")
        self.checkBoxHip.stateChanged.connect(self.filterHip)
        self.checkBoxKnee = QCheckBox("Filter Knee", self)
        self.checkBoxKnee.setObjectName("checkBoxKnee")
        self.checkBoxKnee.stateChanged.connect(self.filterKnee)
        self.checkBoxToe = QCheckBox("Filter Toe", self)
        self.checkBoxToe.setObjectName("checkBoxToe")
        self.checkBoxToe.stateChanged.connect(self.filterToe)
        self.checkBoxLPF = QLabel("LPF")
        self.checkBoxLPF.setObjectName("checkBoxLPF")
        self.checkBoxHPF = QLabel("HPF")
        self.checkBoxHPF.setObjectName("checkBoxHPF")
        self.checkBoxBPF = QLabel("BPF")
        self.checkBoxBPF.setObjectName("checkBoxBPF")
        self.checkBoxBSF = QLabel("BSF")
        self.checkBoxBSF.setObjectName("checkBoxBSF")
        self.checkBoxPoleZero = QLabel()
        self.checkBoxPoleZero.setObjectName("checkBoxPoleZero")
        self.checkBoxPoleZero.setText("PoleZero")

        mainLayout = QHBoxLayout()

        firstRow = QVBoxLayout()
        firstRow1 = QHBoxLayout()
        firstRow1.addWidget(self.labelAnkle)
        firstRow1.addWidget(self.editAnkle)
        firstRow.addLayout(firstRow1)
        firstRow2 = QHBoxLayout()
        firstRow2.addWidget(self.labelHeel)
        firstRow2.addWidget(self.editHeel)
        firstRow.addLayout(firstRow2)
        firstRow3 = QHBoxLayout()
        firstRow3.addWidget(self.labelHip)
        firstRow3.addWidget(self.editHip)
        firstRow.addLayout(firstRow3)
        firstRow4 = QHBoxLayout()
        firstRow4.addWidget(self.labelKnee)
        firstRow4.addWidget(self.editKnee)
        firstRow.addLayout(firstRow4)
        firstRow5 = QHBoxLayout()
        firstRow5.addWidget(self.labelToe)
        firstRow5.addWidget(self.editToe)
        firstRow.addLayout(firstRow5)
        firstRow.addWidget(self.buttonImport)
        firstRow.addWidget(self.buttonFFT)
        firstRow6 = QHBoxLayout()
        firstRow6.addWidget(self.checkBoxLPF)
        firstRow6.addWidget(self.editLPF)
        firstRow.addLayout(firstRow6)
        firstRow.addWidget(self.horizontalSliderLPF)
        firstRow7 = QHBoxLayout()
        firstRow7.addWidget(self.checkBoxHPF)
        firstRow7.addWidget(self.editHPF)
        firstRow.addLayout(firstRow7)
        firstRow.addWidget(self.horizontalSliderHPF)
        firstRow8 = QHBoxLayout()
        firstRow8.addWidget(self.checkBoxBPF)
        firstRow8.addWidget(self.editBPF)
        firstRow.addLayout(firstRow8)
        firstRow.addWidget(self.horizontalSliderBPF)
        firstRow9 = QHBoxLayout()
        firstRow9.addWidget(self.checkBoxBSF)
        firstRow9.addWidget(self.editBSF)
        firstRow.addLayout(firstRow9)
        firstRow.addWidget(self.horizontalSliderBSF)
        firstRow10 = QHBoxLayout()
        firstRow10.addWidget(self.checkBoxPoleZero)
        firstRow10.addWidget(self.editPoleZeroRadius)
        firstRow10.addWidget(self.editPoleZeroTeta)
        firstRow.addLayout(firstRow10)
        firstRow11 = QHBoxLayout()
        firstRow11.addWidget(self.graphPoleZero)
        firstRow12 = QVBoxLayout()
        firstRow12.addWidget(self.horizontalSliderPoleZeroRadius)
        firstRow12.addWidget(self.horizontalSliderPoleZeroTeta)
        firstRow11.addLayout(firstRow12)
        firstRow.addLayout(firstRow11)
        firstRow13 = QHBoxLayout()
        firstRow13.addWidget(self.graphFrequencyResponse)
        firstRow14 = QVBoxLayout()
        firstRow14.addWidget(self.checkBoxAnkle)
        firstRow14.addWidget(self.checkBoxHeel)
        firstRow14.addWidget(self.checkBoxHip)
        firstRow14.addWidget(self.checkBoxKnee)
        firstRow14.addWidget(self.checkBoxToe)
        firstRow13.addLayout(firstRow14)
        firstRow.addLayout(firstRow13)

        mainLayout.addLayout(firstRow)

        secondRow = QVBoxLayout()
        secondRow.addWidget(self.graphAnkle)
        secondRow.addWidget(self.graphHeel)
        secondRow.addWidget(self.graphHip)
        secondRow.addWidget(self.graphKnee)
        secondRow.addWidget(self.graphToe)
        mainLayout.addLayout(secondRow)
        self.setLayout(mainLayout)

    def filterAnkle(self):
        global stateAnkle
        stateAnkle = not stateAnkle

    def filterHeel(self):
        global stateHeel
        stateHeel = not stateHeel

    def filterHip(self):
        global stateHip
        stateHip = not stateHip

    def filterKnee(self):
        global stateKnee
        stateKnee = not stateKnee

    def filterToe(self):
        global stateToe
        stateToe = not stateToe

    def updateLPF(self, value):
        global frequencyLPF
        value /= 10
        frequencyLPF = value
        self.editLPF.setText(str(value))
        self.lowPassFilter()

    def updateHPF(self, value):
        global frequencyHPF
        value /= 10
        frequencyHPF = value
        self.editHPF.setText(str(value))
        self.highPassFilter()

    def updateBPF(self, value):
        global frequencyBPF
        value /= 10
        frequencyBPF = value
        self.editBPF.setText(str(value))
        self.bandPassFilter()

    def updateBSF(self, value):
        global frequencyBSF
        value /= 10
        frequencyBSF = value
        self.editBSF.setText(str(value))
        self.bandStopFilter()

    def updatePoleZeroRadius(self, value):
        global poleZeroRadius, poleZeroTeta
        value /= 100
        poleZeroRadius = value
        self.editPoleZeroRadius.setText(str(poleZeroRadius))
        xPosition = poleZeroRadius * cos(poleZeroTeta * pi / 180)
        yPosition1 = poleZeroRadius * sin(poleZeroTeta * pi / 180)
        yPosition2 = -poleZeroRadius * sin(poleZeroTeta * pi / 180)
        self.graphPoleZero.clear()
        self.graphPoleZero.plot(cos(linspace(0, 2 * pi, 100)), sin(linspace(0, 2 * pi, 100)))
        self.graphPoleZero.plot([xPosition], [yPosition1], symbol="x")
        self.graphPoleZero.plot([xPosition], [yPosition2], symbol="x")
        self.poleZeroFilter()

    def updatePoleZeroTeta(self, value):
        global poleZeroRadius, poleZeroTeta
        poleZeroTeta = value
        self.editPoleZeroTeta.setText(str(value))
        xPosition = poleZeroRadius * cos(poleZeroTeta * pi / 180)
        yPosition1 = poleZeroRadius * sin(poleZeroTeta * pi / 180)
        yPosition2 = -poleZeroRadius * sin(poleZeroTeta * pi / 180)
        self.graphPoleZero.clear()
        self.graphPoleZero.plot(cos(linspace(0, 2 * pi, 100)), sin(linspace(0, 2 * pi, 100)))
        self.graphPoleZero.plot([xPosition], [yPosition1], symbol="x")
        self.graphPoleZero.plot([xPosition], [yPosition2], symbol="x")
        self.poleZeroFilter()

    def importData(self):
        global ankle, heel, hip, knee, toe, p1, p2, p3, p4, p5, nAnkle, \
            nHeel, nHip, nKnee, nToe
        ankle = []
        heel = []
        hip = []
        knee = []
        toe = []
        nAnkle, nHeel, nHip, nKnee, nToe = 0, 0, 0, 0, 0

        with open(self.editAnkle.text(), "r") as fileOpen:
            Lines = fileOpen.readlines()
            for line in Lines:
                ankle += [float(line.strip())]
                nAnkle += 1
        self.graphAnkle.clear()
        p1 = self.graphAnkle.plot(arange(len(ankle)), ankle)
        self.graphAnkle.setTitle("Ankle")
        self.labelAnkle.setText(str(nAnkle))

        with open(self.editHeel.text(), "r") as fileOpen:
            Lines = fileOpen.readlines()
            for line in Lines:
                heel += [float(line.strip())]
                nHeel += 1
        self.graphHeel.clear()
        p2 = self.graphHeel.plot(arange(len(heel)), heel)
        self.graphHeel.setTitle("Heel")
        self.labelHeel.setText(str(nHeel))

        with open(self.editHip.text(), "r") as fileOpen:
            Lines = fileOpen.readlines()
            for line in Lines:
                hip += [float(line.strip())]
                nHip += 1
        self.graphHip.clear()
        p3 = self.graphHip.plot(arange(len(hip)), hip)
        self.graphHip.setTitle("Hip")
        self.labelHip.setText(str(nHip))

        with open(self.editKnee.text(), "r") as fileOpen:
            Lines = fileOpen.readlines()
            for line in Lines:
                knee += [float(line.strip())]
                nKnee += 1
        self.graphKnee.clear()
        p4 = self.graphKnee.plot(arange(len(knee)), knee)
        self.graphKnee.setTitle("Knee")
        self.labelKnee.setText(str(nKnee))

        with open(self.editToe.text(), "r") as fileOpen:
            Lines = fileOpen.readlines()
            for line in Lines:
                toe += [float(line.strip())]
                nToe += 1
        self.graphToe.clear()
        p5 = self.graphToe.plot(arange(len(toe)), toe)
        self.graphToe.setTitle("Toe")
        self.labelToe.setText(str(nToe))

    def FFTData(self):
        global p1, p2, p3, p4, p5, fftAnkle, fftHeel, fftHip, fftKnee, fftToe
        p1.setFftMode(True)
        p2.setFftMode(True)
        p3.setFftMode(True)
        p4.setFftMode(True)
        p5.setFftMode(True)
        fftAnkle = fft.fft(ankle)
        fftHeel = fft.fft(heel)
        fftHip = fft.fft(hip)
        fftKnee = fft.fft(knee)
        fftToe = fft.fft(toe)
        pass

    def lowPassFilter(self):
        nyquistFrequencySampling = 0.5 * frequencySampling
        low = frequencyLPF / nyquistFrequencySampling
        b, a = butter(2, low, 'lowpass', analog=False)
        w, h = freqs(b, a)
        self.graphFrequencyResponse.clear()
        self.graphFrequencyResponse.plot(w, 20 * log10(abs(h))).setLogMode(xMode=True, yMode=False)
        if stateAnkle:
            data = filtfilt(b, a, ankle)
            self.graphAnkle.clear()
            self.graphAnkle.plot(arange(len(ankle)), ankle, pen=(1, 2))
            self.graphAnkle.plot(arange(len(data)), data, pen=(2, 2))
        if stateHip:
            data = filtfilt(b, a, hip)
            self.graphHip.clear()
            self.graphHip.plot(arange(len(hip)), hip, pen=(1, 2))
            self.graphHip.plot(arange(len(data)), data, pen=(2, 2))
        if stateHeel:
            data = filtfilt(b, a, heel)
            self.graphHeel.clear()
            self.graphHeel.plot(arange(len(heel)), heel, pen=(1, 2))
            self.graphHeel.plot(arange(len(data)), data, pen=(2, 2))
        if stateKnee:
            data = filtfilt(b, a, knee)
            self.graphKnee.clear()
            self.graphKnee.plot(arange(len(knee)), knee, pen=(1, 2))
            self.graphKnee.plot(arange(len(data)), data, pen=(2, 2))
        if stateToe:
            data = filtfilt(b, a, toe)
            self.graphToe.clear()
            self.graphToe.plot(arange(len(toe)), toe, pen=(1, 2))
            self.graphToe.plot(arange(len(data)), data, pen=(2, 2))

    def highPassFilter(self):
        nyquistFrequencySampling = 0.5 * frequencySampling
        high = frequencyHPF / nyquistFrequencySampling
        b, a = butter(2, high, 'highpass', analog=False)
        w, h = freqs(b, a)
        self.graphFrequencyResponse.clear()
        self.graphFrequencyResponse.plot(w, -20 * log10(abs(h))).setLogMode(xMode=True, yMode=False)
        if stateAnkle:
            data = filtfilt(b, a, ankle)
            self.graphAnkle.clear()
            self.graphAnkle.plot(arange(len(ankle)), ankle, pen=(1, 2))
            self.graphAnkle.plot(arange(len(data)), data, pen=(2, 2))
        if stateHip:
            data = filtfilt(b, a, hip)
            self.graphHip.clear()
            self.graphHip.plot(arange(len(hip)), hip, pen=(1, 2))
            self.graphHip.plot(arange(len(data)), data, pen=(2, 2))
        if stateHeel:
            data = filtfilt(b, a, heel)
            self.graphHeel.clear()
            self.graphHeel.plot(arange(len(heel)), heel, pen=(1, 2))
            self.graphHeel.plot(arange(len(data)), data, pen=(2, 2))
        if stateKnee:
            data = filtfilt(b, a, knee)
            self.graphKnee.clear()
            self.graphKnee.plot(arange(len(knee)), knee, pen=(1, 2))
            self.graphKnee.plot(arange(len(data)), data, pen=(2, 2))
        if stateToe:
            data = filtfilt(b, a, toe)
            self.graphToe.clear()
            self.graphToe.plot(arange(len(toe)), toe, pen=(1, 2))
            self.graphToe.plot(arange(len(data)), data, pen=(2, 2))

    def bandPassFilter(self):
        nyquistFrequencySampling = 0.5 * frequencySampling
        bandUp = (frequencyBPF + 1) / nyquistFrequencySampling
        bandDown = (frequencyBPF - 1) / nyquistFrequencySampling
        b, a = butter(2, [bandDown, bandUp], 'bandpass', analog=False)
        w, h = freqs(b, a)
        self.graphFrequencyResponse.clear()
        self.graphFrequencyResponse.plot(w, 20 * log10(abs(h))).setLogMode(xMode=True, yMode=False)
        if stateAnkle:
            data = filtfilt(b, a, ankle)
            self.graphAnkle.clear()
            self.graphAnkle.plot(arange(len(ankle)), ankle, pen=(1, 2))
            self.graphAnkle.plot(arange(len(data)), data, pen=(2, 2))
        if stateHip:
            data = filtfilt(b, a, hip)
            self.graphHip.clear()
            self.graphHip.plot(arange(len(hip)), hip, pen=(1, 2))
            self.graphHip.plot(arange(len(data)), data, pen=(2, 2))
        if stateHeel:
            data = filtfilt(b, a, heel)
            self.graphHeel.clear()
            self.graphHeel.plot(arange(len(heel)), heel, pen=(1, 2))
            self.graphHeel.plot(arange(len(data)), data, pen=(2, 2))
        if stateKnee:
            data = filtfilt(b, a, knee)
            self.graphKnee.clear()
            self.graphKnee.plot(arange(len(knee)), knee, pen=(1, 2))
            self.graphKnee.plot(arange(len(data)), data, pen=(2, 2))
        if stateToe:
            data = filtfilt(b, a, toe)
            self.graphToe.clear()
            self.graphToe.plot(arange(len(toe)), toe, pen=(1, 2))
            self.graphToe.plot(arange(len(data)), data, pen=(2, 2))

    def bandStopFilter(self):
        nyquistFrequencySampling = 0.5 * frequencySampling
        stopUp = (frequencyBSF + 1) / nyquistFrequencySampling
        stopDown = (frequencyBSF - 1) / nyquistFrequencySampling
        b, a = butter(2, [stopDown, stopUp], 'bandstop', analog=False)
        w, h = freqs(b, a)
        self.graphFrequencyResponse.clear()
        self.graphFrequencyResponse.plot(w, 20 * log10(abs(h))).setLogMode(xMode=True, yMode=False)
        if stateAnkle:
            data = filtfilt(b, a, ankle)
            self.graphAnkle.clear()
            self.graphAnkle.plot(arange(len(ankle)), ankle, pen=(1, 2))
            self.graphAnkle.plot(arange(len(data)), data, pen=(2, 2))
        if stateHip:
            data = filtfilt(b, a, hip)
            self.graphHip.clear()
            self.graphHip.plot(arange(len(hip)), hip, pen=(1, 2))
            self.graphHip.plot(arange(len(data)), data, pen=(2, 2))
        if stateHeel:
            data = filtfilt(b, a, heel)
            self.graphHeel.clear()
            self.graphHeel.plot(arange(len(heel)), heel, pen=(1, 2))
            self.graphHeel.plot(arange(len(data)), data, pen=(2, 2))
        if stateKnee:
            data = filtfilt(b, a, knee)
            self.graphKnee.clear()
            self.graphKnee.plot(arange(len(knee)), knee, pen=(1, 2))
            self.graphKnee.plot(arange(len(data)), data, pen=(2, 2))
        if stateToe:
            data = filtfilt(b, a, toe)
            self.graphToe.clear()
            self.graphToe.plot(arange(len(toe)), toe, pen=(1, 2))
            self.graphToe.plot(arange(len(data)), data, pen=(2, 2))

    def poleZeroFilter(self):
        global poleZeroRadius
        frequencyResponse = []
        frequencyStart = 0
        frequencyStop = frequencySampling
        xPosition = poleZeroRadius * cos(poleZeroTeta * pi / 180)
        for i in range(frequencySampling):
            w = 2 * pi * i / frequencySampling
            numerator = sqrt((1 - cos(2 * w)) ** 2 + (sin(2 * w)) ** 2)
            denominator = sqrt((1 - 2 * xPosition * cos(w)
                                + (poleZeroRadius ** 2) * cos(2 * w)) ** 2
                               + (2 * xPosition * sin(w)
                                  - (poleZeroRadius ** 2) * sin(2 * w)) ** 2)
            frequencyResponse += [numerator / denominator]
        self.graphFrequencyResponse.clear()
        self.graphFrequencyResponse.plot(linspace(frequencyStart,
                                                  frequencyStop,
                                                  int(frequencySampling / 2)),
                                         frequencyResponse[0:int(frequencySampling / 2)])
        if stateAnkle:
            data = []
            for i in range(len(ankle)):
                if i <= 2:
                    data += [0]
                    continue
                data += [2 * xPosition * data[i - 1] - (poleZeroRadius ** 2) * data[i - 2] + ankle[i]]
                if i > 2:
                    data[i] -= ankle[i - 2]
            data = data / amax(data)
            self.graphAnkle.clear()
            self.graphAnkle.plot(arange(len(ankle)), ankle, pen=(1, 2))
            self.graphAnkle.plot(arange(len(data)), data, pen=(2, 2))
        if stateHip:
            data = []
            for i in range(len(hip)):
                if i <= 2:
                    data += [0]
                    continue
                data += [2 * xPosition * data[i - 1] - (poleZeroRadius ** 2) * data[i - 2] + hip[i]]
                if i > 2:
                    data[i] -= hip[i - 2]
            data = data / amax(data)
            self.graphHip.clear()
            self.graphHip.plot(arange(len(hip)), hip, pen=(1, 2))
            self.graphHip.plot(arange(len(data)), data, pen=(2, 2))
        if stateHeel:
            data = []
            for i in range(len(heel)):
                if i <= 2:
                    data += [0]
                    continue
                data += [2 * xPosition * data[i - 1] - (poleZeroRadius ** 2) * data[i - 2] + heel[i]]
                if i > 2:
                    data[i] -= heel[i - 2]
            data = data / amax(data)
            self.graphHeel.clear()
            self.graphHeel.plot(arange(len(heel)), heel, pen=(1, 2))
            self.graphHeel.plot(arange(len(data)), data, pen=(2, 2))
        if stateKnee:
            data = []
            for i in range(len(knee)):
                if i <= 2:
                    data += [0]
                    continue
                data += [2 * xPosition * data[i - 1] - (poleZeroRadius ** 2) * data[i - 2] + knee[i]]
                if i > 2:
                    data[i] -= knee[i - 2]
            data = data / amax(data)
            self.graphKnee.clear()
            self.graphKnee.plot(arange(len(knee)), knee, pen=(1, 2))
            self.graphKnee.plot(arange(len(data)), data, pen=(2, 2))
        if stateToe:
            data = []
            for i in range(len(toe)):
                if i <= 2:
                    data += [0]
                    continue
                data += [2 * xPosition * data[i - 1] - (poleZeroRadius ** 2) * data[i - 2] + toe[i]]
                if i > 2:
                    data[i] -= toe[i - 2]
            data = data / amax(data)
            self.graphToe.clear()
            self.graphToe.plot(arange(len(toe)), toe, pen=(1, 2))
            self.graphToe.plot(arange(len(data)), data, pen=(2, 2))


if __name__ == '__main__':
    ankle = []
    heel = []
    hip = []
    knee = []
    toe = []
    nAnkle, nHeel, nHip, nKnee, nToe = 0, 0, 0, 0, 0
    p1, p2, p3, p4, p5, p6, p7, p8 = 0, 0, 0, 0, 0, 0, 0, 0
    fftAnkle, fftHeel, fftHip, fftKnee, fftToe = 0, 0, 0, 0, 0
    poleZeroRadius, poleZeroTeta = 0, 0
    stateLPF = False
    stateHPF = False
    stateBPF = False
    stateBSF = False
    statePoleZero = False
    stateAnkle = False
    stateHeel = False
    stateHip = False
    stateKnee = False
    stateToe = False
    frequencySampling = 250
    frequencyLPF, frequencyHPF, frequencyBPF, frequencyBSF = 0, 0, 0, 0
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(Form)
    ui.show()
    sys.exit(app.exec_())
