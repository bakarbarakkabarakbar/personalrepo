import sys
from time import sleep

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtGui
from PyQt5.QtOpenGL import *
from PyQt5.QtWidgets import QOpenGLWidget, QWidget, QPushButton, QHBoxLayout, \
    QVBoxLayout, QSlider, QLabel
from PyQt5 import QtCore, QtWidgets, QtOpenGL
from pyqtgraph import PlotWidget
from math import pi, sin, cos, atan
from numpy import random, array, append, arange, zeros, sqrt
from threading import Timer, Thread, Event


def dampedCosineEquation(time):
    return sin(time) / (time/10), sin(time) / (time/10)


def DEquation(teta, tetadot, phi, phidot):
    tetadotdot = ((-mass * length ** 2 / 3 * tetadot)
                   - (mass * gravitation * centerOfMass * length * cos(phi) * sin(teta))
                   + (mass * length ** 2 * centerOfMass ** 2 * phidot * sin(2 * phi) * tetadot)) \
                  / (mass * length ** 2 * centerOfMass ** 2 * cos(phi ** 2))
    phidotdot = (-1 / 2 * mass * length ** 2 * centerOfMass ** 2 * sin(2 * phi) * tetadot ** 2
                 - mass * gravitation * centerOfMass * length * cos(teta) * sin(phi)) \
                / (mass * length ** 2 * centerOfMass ** 2 + 1 / 3 * mass * length ** 2)
    return tetadotdot, phidotdot


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def PassiveAnimate():
    global t, i, tetaDegree, phiDegree, tetadot, phidot, tetaDegreeFinal, phiDegreeFinal, jointTorque, dampedCosine
    tetadotdot, phidotdot = dampedCosineEquation(t)
    k1teta = 0.5 * dt * tetadotdot
    k1phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = dampedCosineEquation(t + dt / 2)
    k2teta = 0.5 * dt * tetadotdot
    k2phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = dampedCosineEquation(t + dt / 2)
    k3teta = 0.5 * dt * tetadotdot
    k3phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = dampedCosineEquation(t + dt)
    k4teta = 0.5 * dt * tetadotdot
    k4phi = 0.5 * dt * phidotdot

    tetaDegree += [tetaDegree[i] + 1 / 3 * (k1teta + 2 * k2teta + 2 * k3teta + k4teta)]
    phiDegree += [phiDegree[i] + 1 / 3 * (k1phi + 2 * k2phi + 2 * k3phi + k4phi)]

    jointTorque += [sqrt((mass * (length * sin(tetaDegree[i] * pi / 180)) ** 2 / 12
                          + mass * ((length * sin(phiDegree[i] * pi / 180) / 2) ** 2)) ** 2
                         + (mass * (length * cos(tetaDegree[i] * pi / 180)) ** 2 / 12
                            + mass * ((length * cos(phiDegree[i] * pi / 180) / 2) ** 2)) ** 2)]

    tetaDegreeFinal = tetaDegree[i + 1]
    phiDegreeFinal = phiDegree[i + 1]

    dampedCosine += [dampedCosineEquation(t)[0]]

    i += 1
    t += dt

    ui.widget.update()
    ui.graphAbductionAdduction.clear()
    ui.graphAbductionAdduction.plot(arange(len(tetaDegree)), tetaDegree, pen=(1, 2))
    # ui.graphAbductionAdduction.plot(arange(len(dampedCosine)), dampedCosine, pen=(2, 2))
    ui.graphFlexionExtention.clear()
    ui.graphFlexionExtention.plot(arange(len(phiDegree)), phiDegree, pen=(1, 2))
    # ui.graphFlexionExtention.plot(arange(len(dampedCosine)), dampedCosine, pen=(2, 2))
    ui.graphPlane.clear()
    ui.graphPlane.plot(tetaDegree, phiDegree)
    # ui.graphPlane.plot(dampedCosine, dampedCosine, pen=(2, 2))
    ui.graphJointTorque.clear()
    ui.graphJointTorque.plot(arange(len(jointTorque)), jointTorque)


def Animate():
    global t, i, tetaDegree, phiDegree, tetadot, phidot, tetaDegreeFinal, phiDegreeFinal, jointTorque

    tetadotdot, phidotdot = DEquation(tetaDegree[i], tetadot, phiDegree[i], phidot)
    k1teta = 0.5 * dt * tetadotdot
    k1phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = DEquation(tetaDegree[i] + 0.5 * dt * (tetadot + 0.5 * k1teta),
                                      tetadot + k1teta,
                                      phiDegree[i] + 0.5 * dt * (phidot + 0.5 * k1phi),
                                      phidot + k1phi)
    k2teta = 0.5 * dt * tetadotdot
    k2phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = DEquation(tetaDegree[i] + 0.5 * dt * (tetadot + 0.5 * k1teta),
                                      tetadot + k2teta,
                                      phiDegree[i] + 0.5 * dt * (phidot + 0.5 * k1phi),
                                      phidot + k2phi)
    k3teta = 0.5 * dt * tetadotdot
    k3phi = 0.5 * dt * phidotdot

    tetadotdot, phidotdot = DEquation(tetaDegree[i] + dt * (tetadot + k3teta),
                                      tetadot + 2 * k2teta,
                                      phiDegree[i] + dt * (phidot + k3phi),
                                      phidot + 2 * k2phi)
    k4teta = 0.5 * dt * tetadotdot
    k4phi = 0.5 * dt * phidotdot

    tetaDegree += [tetaDegree[i] + dt * (tetadot + 1 / 3 * (k1teta + k2teta + k3teta))]
    tetadot += 1 / 3 * (k1teta + 2 * k2teta + 2 * k3teta + k4teta)
    phiDegree += [phiDegree[i] + dt * (phidot + 1 / 3 * (k1phi + k2phi + k3phi))]
    phidot += 1 / 3 * (k1phi + 2 * k2phi + 2 * k3phi + k4phi)

    jointTorque += [sqrt((mass * (length * sin(tetaDegree[i] * pi / 180)) ** 2 / 12
                          + mass * ((length * sin(phiDegree[i] * pi / 180) / 2) ** 2))**2
                         + (mass * (length * cos(tetaDegree[i] * pi / 180)) ** 2 / 12
                            + mass * ((length * cos(phiDegree[i] * pi / 180) / 2) ** 2))**2)]

    # r = 20 + 10 * sin(2 * pi * 0.5 * t)
    # errorXPID[i+1] = x[i+1] - xPID[i]
    # de = (errorXPID[i+1] - errorXPID[i]) / dt
    # ie += errorXPID[i+1] * dt
    # xPID = kp * errorXPID + kd * de + ki * ie
    #
    # errorYPID[i+1] = y[i+1] - yPID[i]
    # de = (errorYPID[i+1] - errorYPID[i]) / dt
    # ie += errorYPID[i+1] * dt
    # yPID = kp * errorYPID + kd*de + ki*ie

    tetaDegreeFinal = tetaDegree[i + 1]
    phiDegreeFinal = phiDegree[i + 1]

    i += 1
    t += dt

    ui.widget.update()
    ui.graphAbductionAdduction.clear()
    ui.graphAbductionAdduction.plot(arange(len(tetaDegree)), tetaDegree)
    ui.graphFlexionExtention.clear()
    ui.graphFlexionExtention.plot(arange(len(phiDegree)), phiDegree)
    ui.graphPlane.clear()
    ui.graphPlane.plot(tetaDegree, phiDegree)
    ui.graphJointTorque.clear()
    ui.graphJointTorque.plot(arange(len(jointTorque)), jointTorque)


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.resize(1000, 500)
        self.widget = glWidget()
        self.buttonStart = QPushButton('Start Normal', self)
        self.buttonStart.clicked.connect(self.startAnimating)
        self.buttonPassiveStart = QPushButton('Start Passive Test', self)
        self.buttonPassiveStart.clicked.connect(self.startPassiveAnimating)
        self.buttonStop = QPushButton('Stop', self)
        self.buttonStop.clicked.connect(self.stopAnimating)
        self.buttonClear = QPushButton('Clear', self)
        self.buttonClear.clicked.connect(self.clearGraph)
        self.graphJointTorque = PlotWidget(self)
        self.graphJointTorque.setBackground(background=None)
        self.graphJointTorque.setObjectName("graphJointTorque")
        self.graphJointTorque.setTitle("Joint Torque")
        self.graphAbductionAdduction = PlotWidget(self)
        self.graphAbductionAdduction.setBackground(background=None)
        self.graphAbductionAdduction.setObjectName("graphAbductionAdduction")
        self.graphAbductionAdduction.setTitle("Abduction Adduction")
        self.graphError = PlotWidget(self)
        self.graphError.setBackground(background=None)
        self.graphError.setObjectName("graphError")
        self.graphError.setTitle("Error")
        self.graphFlexionExtention = PlotWidget(self)
        self.graphFlexionExtention.setBackground(background=None)
        self.graphFlexionExtention.setObjectName("graphFlexionExtention")
        self.graphFlexionExtention.setTitle("Flexion Extention")
        self.graphPlane = PlotWidget(self)
        self.graphPlane.setBackground(background=None)
        self.graphPlane.setObjectName("graphPlane")
        self.graphPlane.setTitle("Plane")
        self.sliderTeta = QSlider(self)
        self.sliderTeta.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTeta.setRange(-70, 160)
        self.sliderTeta.setSliderPosition(0)
        self.sliderTeta.valueChanged.connect(self.updateTeta)
        self.sliderPhi = QSlider(self)
        self.sliderPhi.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPhi.setRange(-110, 0)
        self.sliderPhi.setSliderPosition(0)
        self.sliderPhi.valueChanged.connect(self.updatePhi)
        self.sliderElbow = QSlider(self)
        self.sliderElbow.setRange(-5, 150)
        self.sliderElbow.setOrientation(QtCore.Qt.Horizontal)
        self.sliderElbow.setSliderPosition(90)
        self.sliderElbow.valueChanged.connect(self.updateElbow)
        self.sliderLabel1 = QLabel(self)
        self.sliderLabel1.setText('90')
        self.sliderLabel2 = QLabel(self)
        self.sliderLabel2.setText('0')
        self.sliderLabel3 = QLabel(self)
        self.sliderLabel3.setText('0')

        mainLayout = QHBoxLayout()
        secondLayout = QVBoxLayout()
        thirdLayout = QVBoxLayout()

        mainLayout.addWidget(self.widget)

        secondLayout.addWidget(self.graphJointTorque)
        secondLayout.addWidget(self.graphError)
        secondLayout.addWidget(self.graphFlexionExtention)
        secondLayout.addWidget(self.graphAbductionAdduction)
        mainLayout.addLayout(secondLayout)

        thirdLayout.addWidget(self.graphPlane)
        thirdLayout.addWidget(self.buttonStart)
        thirdLayout.addWidget(self.buttonPassiveStart)
        thirdLayout.addWidget(self.buttonStop)
        thirdLayout.addWidget(self.buttonClear)
        thirdLayout.addWidget(self.sliderLabel1)
        thirdLayout.addWidget(self.sliderTeta)
        thirdLayout.addWidget(self.sliderLabel2)
        thirdLayout.addWidget(self.sliderPhi)
        thirdLayout.addWidget(self.sliderLabel3)
        thirdLayout.addWidget(self.sliderElbow)
        mainLayout.addLayout(thirdLayout)
        self.setLayout(mainLayout)

    def updateTeta(self, value):
        global tetaValueSlider
        self.sliderLabel1.setText(str(value))
        tetaValueSlider = value
        self.widget.update()

    def updatePhi(self, value):
        global phiValueSlider
        self.sliderLabel2.setText(str(value))
        phiValueSlider = value
        self.widget.update()

    def updateElbow(self, value):
        global elbowDegree
        self.sliderLabel3.setText(str(value))
        elbowDegree = value
        self.widget.update()

    def startAnimating(self):
        timer = RepeatTimer(0.05, Animate)
        timer.start()

    def startPassiveAnimating(self):
        timer2 = RepeatTimer(0.05, PassiveAnimate)
        timer2.start()

    def stopAnimating(self):
        timer.cancel()
        global tetaDegree, tetaDegreePID, tetaDegreeFinal, tetaDegreeError, phiDegree, phiDegreeFinal, phiDegreePID, \
            phiDegreeError, tetadot, phidot, tetaValueSlider, phiValueSlider, elbowDegree, t, i
        tetaDegree = [30 * pi / 180]
        tetaDegreePID = [0]
        tetaDegreeFinal = 0
        tetaDegreeError = []
        phiDegree = [30 * pi / 180]
        phiDegreeFinal = 0
        phiDegreePID = [0]
        phiDegreeError = []
        tetadot = 0
        phidot = 0
        tetaValueSlider = 0
        phiValueSlider = 0
        elbowDegree = 0
        t = 0
        i = 0

    def clearGraph(self):
        self.graphJointTorque.clear()
        self.graphFlexionExtention.clear()
        self.graphAbductionAdduction.clear()
        self.graphPlane.clear()
        self.graphError.clear()


class glWidget(QOpenGLWidget):
    def __init__(self, parent=None, *__args):
        QOpenGLWidget.__init__(self, parent)
        super().__init__(*__args)
        self.setMinimumSize(480, 480)

    def paintGL(self):
        # THIGH INITIAL
        length1 = 0.383
        mass1 = 6.86
        a_1 = 0.42
        inertia1 = 0.133

        # SHANK INITIAL
        length2 = 0.407
        mass2 = 2.76
        a_2 = 0.41
        inertia2 = 0.048

        # FOOT INITIAL
        length3 = 0.149
        mass3 = 0.89
        a_3 = 0.4
        inertia3 = 0.004

        global tetaDegreeFinal, phiDegreeFinal
        tetaDegreeCalibrated = tetaDegreeFinal * 10 + tetaValueSlider + 90
        phiDegreeCalibrated = phiDegreeFinal * 10 + phiValueSlider
        tetaRadian = tetaDegreeCalibrated * pi / 180
        phiRadian = phiDegreeCalibrated * pi / 180
        elbowRadian = elbowDegree * pi / 180

        xPosition = 0
        yPosition = 1 / 2
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

        # 1. UpperJoint
        glPushMatrix()
        glTranslatef(xPosition, yPosition, zPosition)
        gluSphere(gluNewQuadric(), 0.09, 32, 32)
        # glPopMatrix()

        # 2. UpperArm
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        glRotatef(tetaDegreeCalibrated, 1.0, 0.0, 0.0)
        glRotatef(phiDegreeCalibrated, 0.0, 1.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.090, 0.072, length1, 32, 32)
        # glPopMatrix()

        # 3. Elbow
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef(length1 * sin(tetaRadian) * sin(phiRadian),
        #              -length1 * sin(tetaRadian) * cos(phiRadian),
        #              length1 * cos(tetaRadian))
        glTranslatef(0, 0, length1)
        gluSphere(gluNewQuadric(), 0.075, 32, 32)
        # glPopMatrix()

        # 4. Lower Arm
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef(length1 * sin(tetaRadian) * sin(phiRadian),
        #              -length1 * sin(tetaRadian) * cos(phiRadian),
        #              length1 * cos(tetaRadian))
        glRotatef(elbowDegree, 1.0, 0.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.065, 0.035, length2, 32, 32)
        # glPopMatrix()

        # 5. Wrist
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef((length1 + length2) * sin(tetaRadian) * sin(phiRadian),
        #              -(length1 + length2) * sin(tetaRadian) * cos(phiRadian),
        #              (length1 + length2) * cos(tetaRadian))
        glTranslatef(0, 0, length2)
        # glRotatef(-90, 1.0, 0.0, 0.0)
        gluSphere(gluNewQuadric(), 0.040, 32, 32)
        # glPopMatrix()

        # 6. Palm
        tp = 0.130
        tl = 0.1
        tt = 0.0175
        # flatten = atan(0.025 / (length3 * 5))

        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef(length1 * sin(phiRadian), -length1 * cos(teta3Radian), -length1 * cos(tetaRadian))
        # glTranslatef(length2 * sin(phiRadian), -length2 * cos(teta3Radian), -length2 * cos(tetaRadian))
        # glRotatef(tetaDegreeCalibrated, 1.0, 0.0, 0.0)
        # glRotatef(phiDegree, 0.0, 1.0, 0.0)

        # BackHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, tp)
        glEnd()

        # FrontHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, tp)
        glEnd()

        # LeftSideHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, tp)
        glEnd()

        # RightSideHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, tt, tp)
        glEnd()

        # DownHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, tp)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, tp)
        glEnd()

        # UpHand
        glBegin(GL_POLYGON)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(tl, -tt, 0)
        glColor3f(1 / 3, 1 / 3, 1 / 3)
        glVertex3f(-tl, -tt, 0)
        glEnd()

        # FirstSegmentFinger
        fingerPosition0 = 0.023
        fingerPosition1 = 0.025
        fingerPosition2 = 0.027
        fingerSpace = 0.05

        # Thumb
        glTranslate(-2 * fingerSpace, 0, tp)
        gluCylinder(gluNewQuadric(), 0.0095, 0.0095, fingerPosition0, 32, 10)
        gluSphere(gluNewQuadric(), 0.0097, 32, 32)

        # IndexFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.0075, 0.0075, fingerPosition0, 32, 10)
        gluSphere(gluNewQuadric(), 0.0077, 32, 32)

        # MiddleFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.0080, 0.0075, fingerPosition0, 32, 10)
        gluSphere(gluNewQuadric(), 0.0080, 32, 32)

        # ThirdFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition0, 32, 10)
        gluSphere(gluNewQuadric(), 0.0072, 32, 32)

        # LittleFinger
        glTranslate(fingerSpace, 0, 0)
        gluSphere(gluNewQuadric(), 0.0072, 32, 32)
        gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition0, 32, 10)

        # SecondSegmentFinger
        # Thumb
        glTranslate(-4 * fingerSpace, 0, fingerPosition1)
        gluCylinder(gluNewQuadric(), 0.0095, 0.0095, fingerPosition1, 32, 32)
        gluSphere(gluNewQuadric(), 0.0097, 32, 32)

        # IndexFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.0075, 0.0075, fingerPosition1, 32, 32)
        gluSphere(gluNewQuadric(), 0.0077, 32, 32)

        # MiddleFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 32)
        gluSphere(gluNewQuadric(), 0.0072, 32, 32)

        # ThirdFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 32)
        gluSphere(gluNewQuadric(), 0.0072, 32, 32)

        # LittleFinger
        glTranslate(fingerSpace, 0, 0)
        glRotate(25, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 32)
        gluSphere(gluNewQuadric(), 0.0072, 32, 32)

        # ThirdSegmentFinger
        # IndexFinger
        glTranslate(-3 * fingerSpace, 0, fingerPosition2)
        gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
        gluSphere(gluNewQuadric(), 0.0077, 32, 32)

        # MiddleFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
        gluSphere(gluNewQuadric(), 0.0077, 32, 32)

        # ThirdFinger
        glTranslate(fingerSpace, 0, 0)
        gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
        gluSphere(gluNewQuadric(), 0.0077, 32, 32)
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
    mass = 1
    length = 2
    gravitation = 9.8
    centerOfMass = 0.507
    tetaDegree = [30*pi/180]
    tetaDegreePID = [0]
    tetaDegreeFinal = 0
    tetaDegreeError = []
    phiDegree = [30*pi/180]
    phiDegreeFinal = 0
    phiDegreePID =[0]
    phiDegreeError = []
    jointTorque = []
    dampedCosine = [0]
    tetadot = 0
    phidot = 0
    tetaValueSlider = 0
    phiValueSlider = 0
    elbowDegree = 0

    dt = 0.0235
    t = 0.001
    kp = 1
    kd = 1
    ki = 0.05
    ie = 0.0
    i = 0

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(Form)
    ui.show()
    sys.exit(app.exec_())
