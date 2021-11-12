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
from numpy import random, array, append, arange, zeros
from threading import Timer, Thread, Event


def ODEquation(y, yDot, x, xDot):
    # return -1.5*yDot-y+2*xDot+x;
    return -1.5*yDot - y +2*xDot + x


def DEquation(x, y):
    # return -0.5*yDot-y+x;
    return sin(x)


def DEquation1(y, x):
    # return -14*yDot-45*y+x;
    return cos(y)


def movingEquation():
    global start, teta1Degree, teta2Degree


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def Animate():
    global t, i, teta1Degree, teta2Degree
    # RUNGEKUTTA
    k1 = dt * DEquation(y[i], yDot[i])
    k2 = dt * DEquation(y[i] + dt / 2, yDot[i] + k1 / 2)
    k3 = dt * DEquation(y[i] + dt / 2, yDot[i] + k2 / 2)
    k4 = dt * DEquation(y[i] + dt, yDot[i] + k3)
    yDot[i + 1] = yDot[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    y[i + 1] = y[i] + dt

    k1 = dt * DEquation1(x[i], xDot[i])
    k2 = dt * DEquation1(x[i] + dt / 2, xDot[i] + k1 / 2)
    k3 = dt * DEquation1(x[i] + dt / 2, xDot[i] + k2 / 2)
    k4 = dt * DEquation1(x[i] + dt, xDot[i] + k3)
    xDot[i + 1] = xDot[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    x[i + 1] = x[i] + dt

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

    teta1Degree = xDot[i + 1]*10-5 + teta1ValueSlider
    teta2Degree = yDot[i + 1]*10-5 + teta2ValueSlider

    i += 1
    t += dt

    ui.widget.update()
    ui.graphAbductionAdduction.clear()
    ui.graphAbductionAdduction.plot(x, xDot)
    ui.graphFlexionExtention.clear()
    ui.graphFlexionExtention.plot(y, yDot)


class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.widget = glWidget()
        self.buttonStart = QPushButton('Start', self)
        self.buttonStart.clicked.connect(self.startAnimating)
        self.buttonStop = QPushButton('Stop', self)
        self.buttonStop.clicked.connect(self.stopAnimating)
        self.buttonClear = QPushButton('Clear', self)
        self.buttonClear.clicked.connect(self.clearGraph)
        self.graphJointTorque = PlotWidget(self)
        self.graphJointTorque.setBackground(background=None)
        self.graphJointTorque.setObjectName("graphJointTorque")
        self.graphAbductionAdduction = PlotWidget(self)
        self.graphAbductionAdduction.setBackground(background=None)
        self.graphAbductionAdduction.setObjectName("graphAbductionAdduction")
        self.graphError = PlotWidget(self)
        self.graphError.setBackground(background=None)
        self.graphError.setObjectName("graphError")
        self.graphFlexionExtention = PlotWidget(self)
        self.graphFlexionExtention.setBackground(background=None)
        self.graphFlexionExtention.setObjectName("graphFlexionExtention")
        self.graphTransversalPlane = PlotWidget(self)
        self.graphTransversalPlane.setBackground(background=None)
        self.graphTransversalPlane.setObjectName("graphTransversalPlane")
        self.sliderTeta1 = QSlider(self)
        self.sliderTeta1.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTeta1.setRange(-70, 160)
        self.sliderTeta1.setSliderPosition(0)
        self.sliderTeta1.valueChanged.connect(self.updateTeta1)
        self.sliderTeta2 = QSlider(self)
        self.sliderTeta2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTeta2.setRange(-110, 0)
        self.sliderTeta2.setSliderPosition(0)
        self.sliderTeta2.valueChanged.connect(self.updateTeta2)
        self.sliderElbow = QSlider(self)
        self.sliderElbow.setRange(-5, 150)
        self.sliderElbow.setOrientation(QtCore.Qt.Horizontal)
        self.sliderElbow.setSliderPosition(0)
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
        secondLayout.addWidget(self.graphTransversalPlane)
        secondLayout.addWidget(self.graphFlexionExtention)
        secondLayout.addWidget(self.graphAbductionAdduction)
        secondLayout.addWidget(self.graphError)
        mainLayout.addLayout(secondLayout)

        thirdLayout.addWidget(self.buttonStart)
        thirdLayout.addWidget(self.buttonStop)
        thirdLayout.addWidget(self.buttonClear)
        thirdLayout.addWidget(self.sliderLabel1)
        thirdLayout.addWidget(self.sliderTeta1)
        thirdLayout.addWidget(self.sliderLabel2)
        thirdLayout.addWidget(self.sliderTeta2)
        thirdLayout.addWidget(self.sliderLabel3)
        thirdLayout.addWidget(self.sliderElbow)
        mainLayout.addLayout(thirdLayout)
        self.setLayout(mainLayout)

    def updateTeta1(self, value):
        global teta1Degree, teta1ValueSlider
        self.sliderLabel1.setText(str(value))
        teta1Degree = value
        teta1ValueSlider = value
        self.widget.update()

    def updateTeta2(self, value):
        global teta2Degree, teta2ValueSlider
        self.sliderLabel2.setText(str(value))
        teta2Degree = value
        teta2ValueSlider = value
        self.widget.update()

    def updateElbow(self, value):
        global elbowDegree
        self.sliderLabel3.setText(str(value))
        elbowDegree = value
        self.widget.update()

    def startAnimating(self):
        global timer
        timer = RepeatTimer(0.1, Animate)
        timer.start()

    def stopAnimating(self):
        global y, yPID, errorYPID, yDot, x, xDot, xPID, errorXPID
        y = zeros(n)
        yPID = zeros(n)
        errorYPID = zeros(n)
        yDot = zeros(n)
        x = zeros(n)
        xDot = zeros(n)
        xPID = zeros(n)
        errorXPID = zeros(n)
        timer.cancel()

    def clearGraph(self):
        self.graphJointTorque.clear()
        self.graphFlexionExtention.clear()
        self.graphAbductionAdduction.clear()


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

        global teta1Degree, teta2Degree, alphaDegree, beta1Degree, beta2Degree
        teta1DegreeCalibrated = teta1Degree + 90
        teta1Radian = teta1DegreeCalibrated * pi / 180
        teta2Radian = teta2Degree * pi / 180
        elbowRadian = elbowDegree * pi / 180
        beta1Radian = beta1Degree * pi / 180
        beta2Radian = beta2Degree * pi / 180

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
        glRotatef(teta1DegreeCalibrated, 1.0, 0.0, 0.0)
        glRotatef(teta2Degree, 0.0, 1.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.090, 0.072, length1, 32, 32)
        # glPopMatrix()

        # 3. Elbow
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef(length1 * sin(teta1Radian) * sin(teta2Radian),
        #              -length1 * sin(teta1Radian) * cos(teta2Radian),
        #              length1 * cos(teta1Radian))
        glTranslatef(0, 0, length1)
        gluSphere(gluNewQuadric(), 0.075, 32, 32)
        # glPopMatrix()

        # 4. Lower Arm
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef(length1 * sin(teta1Radian) * sin(teta2Radian),
        #              -length1 * sin(teta1Radian) * cos(teta2Radian),
        #              length1 * cos(teta1Radian))
        glRotatef(elbowDegree, 1.0, 0.0, 0.0)
        gluCylinder(gluNewQuadric(), 0.065, 0.035, length2, 32, 32)
        # glPopMatrix()

        # 5. Wrist
        # glPushMatrix()
        # glTranslatef(xPosition, yPosition, zPosition)
        # glTranslatef((length1 + length2) * sin(teta1Radian) * sin(teta2Radian),
        #              -(length1 + length2) * sin(teta1Radian) * cos(teta2Radian),
        #              (length1 + length2) * cos(teta1Radian))
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
        # glTranslatef(length1 * sin(teta2Radian), -length1 * cos(teta3Radian), -length1 * cos(teta1Radian))
        # glTranslatef(length2 * sin(teta2Radian), -length2 * cos(teta3Radian), -length2 * cos(teta1Radian))
        # glRotatef(teta1DegreeCalibrated, 1.0, 0.0, 0.0)
        # glRotatef(teta2Degree, 0.0, 1.0, 0.0)

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
    teta1Degree = 0
    teta2Degree = 0
    teta1ValueSlider = 0
    teta2ValueSlider = 0
    elbowDegree = 0
    beta1Degree = 0
    beta2Degree = 0

    n = 5000
    y = zeros(n)
    yPID = zeros(n)
    errorYPID = zeros(n)
    yDot = zeros(n)
    x = zeros(n)
    xDot = zeros(n)
    xPID = zeros(n)
    errorXPID = zeros(n)
    dt = 0.1
    t = 0
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
