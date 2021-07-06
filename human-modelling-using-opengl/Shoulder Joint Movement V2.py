from Window import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from math import pi, sin, cos, atan
from OpenGL.GL import *
from OpenGL.GLU import *


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

class shoulderjointmovement(Ui_Dialog):
    def __init__(self):
        Ui_Dialog.__init__(self)

    def handleStart(self):
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        self.lineEditZ.setText(str(x + y))

    def handleClear(self):
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        self.lineEditZ.setText(str(x + y))

    def handleClear(self):
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        self.lineEditZ.setText(str(x + y))


def render(teta1, teta2, teta3):
    mat_specular = [8.0, 8.0, 1.0, 0.0]
    mat_shininess = 40.0
    light_position = [120.6, 14.0, 41.0, 10.7]

    glLoadIdentity()

    glShadeModel(GL_SMOOTH)  # // Enables Smooth Color Shading
    glClearDepth(1.0)  # // Depth Buffer Setup
    glEnable(GL_DEPTH_TEST)  # // Enable Depth Buffer
    glDepthFunc(GL_LESS)  # // The Type Of Depth Test To Do

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_BACK, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glMaterialfv(GL_BACK, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT3, GL_SPECULAR, mat_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position)
    glLightfv(GL_LIGHT2, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glDepthFunc(GL_LEQUAL)

    xPosition = -2 / 5
    yPosition = -1 / 5
    zPosition = -15 / 5

    teta1Degree = (teta1 * 180) / pi
    teta2Degree = (teta2 * 180) / pi
    teta3Degree = (teta3 * 180) / pi

    tp = 0.130  # ; //panjang tangan
    tl = 0.1  # ; //lebar tangan
    tt = 0.0175  # ;//tebal tangan

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(xPosition, yPosition, zPosition)
    gluSphere(gluNewQuadric(), 0.09, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xPosition, yPosition, zPosition)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(teta1Degree, 0.0, 1.0, 0.0)
    gluCylinder(gluNewQuadric(), 0.090, 0.075, length1, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xPosition, yPosition, zPosition)
    glTranslatef(length1 * sin(teta1), -length1 * cos(teta1), 0.0)
    gluSphere(gluNewQuadric(), 0.080, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xPosition, yPosition, zPosition)
    glTranslatef(length1 * sin(teta1), -length1 * cos(teta1), 0.0)
    glRotatef(-teta2Degree, 0.0, 0.0, 1.0)
    glTranslatef(-length1 * sin(teta1), length1 * cos(teta1), 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(teta1Degree, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, length1)
    gluCylinder(gluNewQuadric(), 0.065, 0.035, length2, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xPosition, yPosition, zPosition)
    glTranslatef((length1 * sin(teta1) - length2 * sin(teta2 - teta1)),
                 -(length1 * cos(teta1) + length2 * cos(teta2 - teta1)), 0.0)
    gluSphere(gluNewQuadric(), 0.040, 32, 32)
    glPopMatrix()

    glPushMatrix()
    flatten = atan(0.025 / (length3 * 5))
    glTranslatef(xPosition, yPosition, zPosition)
    glTranslatef((length1 * sin(teta1) - length2 * sin(teta2 - teta1)),
                 -(length1 * cos(teta1) + length2 * cos(teta2 - teta1)), 0.0)
    glRotatef(90 - (teta2Degree - teta1Degree + teta3Degree + ((flatten * 180) / pi)), 0.0, 0.0, 1.0)
    glTranslatef(-(length1 * sin(teta1) - length2 * sin(teta2 - teta1)),
                 (length1 * cos(teta1) + length2 * cos(teta2 - teta1)), 0.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -(length1 * cos(teta1) + length2 * cos(teta2 - teta1)),
                 (length1 * sin(teta1) - length2 * sin(teta2 - teta1)))

    # hand
    glRotate(-180, 1, 0, 0)
    glRotate(-45, 0, 0, 1)
    # // gldisable(gl_lighting)
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

    glBegin(GL_POLYGON)  # ;     //dasar -tt
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)
    glEnd()

    glBegin(GL_POLYGON)  # ;   //samping kiri -t1
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)
    glEnd()

    glBegin(GL_POLYGON)  #samping kanan +tl
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)
    glEnd()

    glBegin(GL_POLYGON)  #depan sumbu z +tp
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)
    glEnd()

    glBegin(GL_POLYGON)  #belakang sumbu z 0
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)
    glEnd()

    # {first segment}
    # {centre fingers}
    fingerPosition0 = 0.025
    fingerPosition1 = 0.023
    fingerPosition2 = 0.027
    glTranslate(0, 0, tp)
    glRotate(360, 1, 0, 0)
    glEnable(GL_LIGHTING)
    gluCylinder(gluNewQuadric(), 0.0080, 0.0075, fingerPosition0, 32, 10)
    gluSphere(gluNewQuadric(), 0.0080, 32, 32)

    # {pointer finger}
    jarispace = 0.05
    glTranslate(jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, fingerPosition0, 32, 10)
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)

    # {tumb}
    glTranslate(jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, fingerPosition0, 32, 10)
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)

    # {jari manis}
    glTranslate(-3 * jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition0, 32, 10)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)

    # {kelingking}
    glTranslate(-jarispace, 0, 0)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)
    gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition0, 32, 10)

    # {second segment}
    # {kelingking}
    glTranslate(0, 0, fingerPosition0)
    glRotate(10, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 10)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)

    glTranslate(0, 0, fingerPosition1)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)

    glTranslate(0, 0, -fingerPosition1)

    # {jari manis}
    glTranslate(jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 32)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)

    # {jari tengah}
    glTranslate(jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.007, 0.007, fingerPosition1, 32, 10)
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)

    # {jari telunjuk}
    glTranslate(jarispace, 0, 0)
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, fingerPosition1, 32, 10)
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)

    # {tumb}
    glTranslate(jarispace, 0, 0)
    # //fingerPosition1:=0.15
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, fingerPosition1, 32, 10)
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)
    glTranslate(0, 0, fingerPosition1)
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)

    # {third segment}

    # {telunjuk}
    glTranslate(-jarispace, 0, 0)
    glRotate(10, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)
    glTranslate(0, 0, fingerPosition2)
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)

    # {jaritengah}
    glTranslate(-jarispace, 0, -fingerPosition2)
    glPushMatrix()
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)
    glTranslate(0, 0, fingerPosition2)
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)

    # {jari manis}
    glTranslate(-jarispace, 0, -fingerPosition2)
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, fingerPosition2, 32, 10)
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)
    glTranslate(0, 0, fingerPosition2)
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)
    glPopMatrix()
    glPopMatrix()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
