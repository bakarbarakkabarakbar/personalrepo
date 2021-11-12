import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtGui
from PyQt5.QtOpenGL import *
from PyQt5.QtWidgets import QOpenGLWidget, QWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QSlider, QLabel
from PyQt5 import QtCore, QtWidgets, QtOpenGL
from pyqtgraph import PlotWidget
from math import pi, sin, cos, atan
from numpy import random, array, append, arange, zeros, sqrt, tanh
from threading import Timer, Thread, Event
from scipy.signal import square


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def DEquation(teta, tetadot):
    return gravity / lengthLowerLeg * sin(teta * pi / 180)


def animate():
    global kneeDegree, jointTorque, ankleDegree, massLowerLeg, massBottomLeg, i, tetadotdot, tetadot
    k1teta = 0.5 * dt * DEquation(kneeDegree[i], tetadot)
    k2teta = 0.5 * dt * DEquation(kneeDegree[i], tetadot)
    k3teta = 0.5 * dt * DEquation(kneeDegree[i], tetadot)
    k4teta = 0.5 * dt * DEquation(kneeDegree[i], tetadot)

    tetadot += 1 / 3 * (k1teta + 2 * k2teta + 2 * k3teta + k4teta)

    kneeDegree += [kneeDegree[i] + tetadot]

    jointTorque += [((massLowerLeg + massBottomLeg) * (lengthLowerLeg * sin(kneeDegree[i] * pi / 180)) ** 2 / 12
                          + (massLowerLeg + massBottomLeg)
                          * ((lengthLowerLeg * cos(kneeDegree[i] * pi / 180) / 2) ** 2)) ** 2]
    ankleDegree += [ankleDegree[i]]

    i += 1
    ui.widget.update()
    ui.graphKneeJointAngle.clear()
    ui.graphJointTorque.clear()
    ui.graphAnkleJointAngle.clear()
    ui.graphKneeJointAngle.plot(arange(len(kneeDegree)), kneeDegree)
    ui.graphJointTorque.plot(arange(len(jointTorque)), jointTorque)
    ui.graphAnkleJointAngle.plot(arange(len(ankleDegree)), ankleDegree)


def animateTestedSystem():
    global i, square, forceLength, forceVelocity
    i += 1
    square += [squareFunction(i)]
    forceLength += [function(square[i-1])]
    forceVelocity += [functionTwo(i)]
    ui.graphKneeJointAngle.clear()
    ui.graphJointTorque.clear()
    ui.graphAnkleJointAngle.clear()
    ui.graphJointTorque.plot(arange(len(square)), square)
    ui.graphKneeJointAngle.plot(arange(len(forceLength)), forceLength)
    ui.graphAnkleJointAngle.plot(arange(len(forceVelocity)), forceVelocity)


def squareFunction(teta):
    if cos(teta * pi / 90) > 0.5:
        return 1
    if cos(teta * pi / 90) < 0.5:
        return 0


def function(signal):
    return 0.5*tanh(15*(signal-0.5)) + 0.5


def functionTwo(v):
    if squareFunction(teta) < function(squareFunction(teta)):
        return (vMaximum - v)/(vMaximum + 2.5*v)
    else:
        return 1.3 - 0.3 * (vMaximum + 2.5 * v) / (vMaximum + 2.5**2 * v)


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.resize(700, 500)
        self.widget = glWidget()
        self.buttonStart = QPushButton('Start', self)
        self.buttonStart.clicked.connect(self.startAnimating)
        self.buttonStartTestedSystem = QPushButton('Start Tested System', self)
        self.buttonStartTestedSystem.clicked.connect(self.startTestedSystem)
        self.buttonClear = QPushButton('Clear', self)
        self.buttonClear.clicked.connect(self.clearGraph)
        self.graphJointTorque = PlotWidget(self)
        self.graphJointTorque.setBackground(background=None)
        self.graphJointTorque.setObjectName("graphJointTorque")
        self.graphKneeJointAngle = PlotWidget(self)
        self.graphKneeJointAngle.setBackground(background=None)
        self.graphKneeJointAngle.setObjectName("graphKneeJointAngle")
        self.graphAnkleJointAngle = PlotWidget(self)
        self.graphAnkleJointAngle.setBackground(background=None)
        self.graphAnkleJointAngle.setObjectName("graphAnkleJointAngle")
        self.sliderKneeJointAngle = QSlider(self)
        self.sliderKneeJointAngle.setOrientation(QtCore.Qt.Horizontal)
        self.sliderKneeJointAngle.setRange(0, 135)
        self.sliderKneeJointAngle.setSliderPosition(0)
        self.sliderKneeJointAngle.valueChanged.connect(self.updateKneeJointAngle)
        self.sliderAnkleJointAngle = QSlider(self)
        self.sliderAnkleJointAngle.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAnkleJointAngle.setRange(-20, 20)
        self.sliderAnkleJointAngle.setSliderPosition(0)
        self.sliderAnkleJointAngle.valueChanged.connect(self.updateAnkleJointAngle)
        self.sliderLabel1 = QLabel(self)
        self.sliderLabel1.setText('Ankle')
        self.sliderLabel2 = QLabel(self)
        self.sliderLabel2.setText('0')
        self.sliderLabel3 = QLabel(self)
        self.sliderLabel3.setText('Knee')
        self.sliderLabel4 = QLabel(self)
        self.sliderLabel4.setText('0')

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.widget)

        secondRow = QVBoxLayout()
        secondRow.addWidget(self.graphJointTorque)
        secondRow.addWidget(self.graphKneeJointAngle)
        secondRow.addWidget(self.graphAnkleJointAngle)
        secondRow.addWidget(self.buttonStart)
        secondRow.addWidget(self.buttonStartTestedSystem)
        secondRow.addWidget(self.buttonClear)
        secondRow1 = QHBoxLayout()
        secondRow1.addWidget(self.sliderLabel1)
        secondRow1.addWidget(self.sliderLabel2)
        secondRow1.addWidget(self.sliderAnkleJointAngle)
        secondRow.addLayout(secondRow1)
        secondRow2 = QHBoxLayout()
        secondRow2.addWidget(self.sliderLabel3)
        secondRow2.addWidget(self.sliderLabel4)
        secondRow2.addWidget(self.sliderKneeJointAngle)
        secondRow.addLayout(secondRow2)
        mainLayout.addLayout(secondRow)
        self.setLayout(mainLayout)

    def updateKneeJointAngle(self, value):
        global kneeDegree, ankleDegree, i
        self.sliderLabel4.setText(str(value))
        kneeDegree += [value]
        ankleDegree += [ankleDegree[i]]
        ui.graphKneeJointAngle.clear()
        ui.graphAnkleJointAngle.clear()
        ui.graphKneeJointAngle.plot(arange(len(kneeDegree)), kneeDegree)
        ui.graphAnkleJointAngle.plot(arange(len(ankleDegree)), ankleDegree)
        i += 1
        self.widget.update()

    def updateAnkleJointAngle(self, value):
        global ankleDegree, kneeDegree, i
        self.sliderLabel2.setText(str(value))
        ankleDegree += [value]
        kneeDegree += [kneeDegree[i]]
        ui.graphAnkleJointAngle.clear()
        ui.graphKneeJointAngle.clear()
        ui.graphAnkleJointAngle.plot(arange(len(ankleDegree)), ankleDegree)
        ui.graphKneeJointAngle.plot(arange(len(kneeDegree)), kneeDegree)
        i += 1
        self.widget.update()

    def startAnimating(self):
        global timer, i
        i = 0
        timer = RepeatTimer(0.1, animate)
        timer.start()

    def startTestedSystem(self):
        global timer, i
        i = 0
        timer = RepeatTimer(0.1, animateTestedSystem)
        timer.start()

    def clearGraph(self):
        ui.graphAnkleJointAngle.clear()
        ui.graphKneeJointAngle.clear()
        ui.graphJointTorque.clear()


class glWidget(QOpenGLWidget):
    def __init__(self, parent=None, *__args):
        QOpenGLWidget.__init__(self, parent)
        super().__init__(*__args)
        self.setMinimumSize(480, 480)

    def paintGL(self):
        global kneeDegree, hipDegree, ankleDegree, i
        kneeRadian = (180 - kneeDegree[i]) * pi / 180
        hipRadian = hipDegree * pi / 180
        footRadian = ankleDegree[i] * pi / 180

        xPosition = -2 / 3
        yPosition = 1 / 3
        zPosition = -8 / 5

        mat_specular = [8.0, 8.0, 1.0, 0.0]
        mat_shininess = 40.0
        light_position = [20, 14.0, 41.0, 10.7]

        glShadeModel(GL_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_3D)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glDepthFunc(GL_LEQUAL)

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_BACK, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
        glMaterialfv(GL_BACK, GL_SHININESS, mat_shininess)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glLoadIdentity()

        # Hip
        glPushMatrix()
        glTranslatef(xPosition, yPosition, zPosition)
        gluSphere(gluNewQuadric(), 0.09, 32, 32)

        # Upper Leg
        glRotatef(90, 1.0, 0.0, 0.0)
        glRotatef(hipDegree, 0.0, 1.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.090, 0.072, lengthUpperLeg, 32, 32)
        glPopMatrix()

        # Knee
        glPushMatrix()
        glTranslatef(xPosition, yPosition, zPosition)
        glTranslatef(lengthUpperLeg, 0, 0)
        glRotatef(90, 1.0, 0.0, 0.0)
        glRotatef(180-kneeDegree[i], 0.0, 1.0, 0.0)
        gluSphere(gluNewQuadric(), 0.075, 32, 32)

        # Lower Leg
        gluCylinder(gluNewQuadric(), 0.065, 0.035, lengthLowerLeg, 32, 32)
        glPopMatrix()

        # Foot
        glPushMatrix()
        glTranslatef(xPosition, yPosition, zPosition)
        glTranslatef(lengthUpperLeg, 0, 0)
        glRotatef(90, 1.0, 0.0, 0.0)
        glTranslatef(lengthLowerLeg*sin(kneeRadian), 0, lengthLowerLeg*cos(kneeRadian))
        gluSphere(gluNewQuadric(), 0.040, 32, 32)
        glRotatef(ankleDegree[i] + 270 - kneeDegree[i], 0.0, 1.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.045, 0.025, lengthBottomLeg, 32, 32)
        glPopMatrix()

    def initializeGL(self):
        glClearColor(0, 0, 0, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, 1.25, 1, 10)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)


if __name__ == '__main__':
    hipDegree = 90
    ankleDegree = [0]
    kneeDegree = [90]
    kneeDot = []
    jointTorque = []
    square = []
    forceLength = []
    forceVelocity = []
    gravity = 9.8
    teta, tetadot, tetadotdot = 0, 0, 0
    lengthOptimum = 0
    vMaximum = 0

    dt = 0.0235
    t = 0.001
    i = 0
    timer = 0

    # Upper Leg
    lengthUpperLeg = 0.66
    massUpperLeg = 48.68
    centerOfMassUpperLeg = 0.398
    inertiaUpperLeg = 1.767

    # Lower Leg
    lengthLowerLeg = 0.599
    massLowerLeg = 20.28
    centerOfMassLowerLeg = 0.413
    inertiaLowerLeg = 0.606

    # Bottom Leg
    lengthBottomLeg = 0.18
    massBottomLeg = 6.98
    centerOfMassBottomLeg = 0.4
    inertiaBottomLeg = 0.018

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(Form)
    ui.show()
    sys.exit(app.exec_())