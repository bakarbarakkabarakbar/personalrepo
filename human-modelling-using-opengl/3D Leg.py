import pygame
import tkinter as tk
from tkinter import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # , NavigationToolbar2Tk
from matplotlib.figure import Figure

root = tk.Tk()
root.geometry("1300x600")
root.config(bg="skyblue")

# declare canvas
fig1 = Figure(figsize=(4, 2.5))

# declare labelframe
utama = LabelFrame(root, text="OPENGL", padx=15, pady=10)
utama.place(x=10, y=40)

# declare frame
embed = tk.Frame(utama, width=800, height=500)  # creates embed frame for pygame window
embed.pack(side=LEFT)  # packs window to the left

labelGab = LabelFrame(utama, text="INPUT", padx=45, pady=10)
labelGab.pack()

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((800, 500), )
screen.fill(pygame.Color(255, 255, 0))


def create():
    global xpos, ypos, zpos, rotangle, rotangle1, rotangle2, f0, f1, f2, f3, time

    theta = 30 * pi / 180
    phi = 20 * pi / 180
    thetadot = 0
    phidot = 0

    # SetupPixelFormat()
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 1.0)  # // Black Background
    glShadeModel(GL_SMOOTH)  # // Enables Smooth Color Shading
    glClearDepth(1.0)  # // Depth Buffer Setup
    glEnable(GL_DEPTH_TEST)  # // Enable Depth Buffer
    glDepthFunc(GL_LESS)  # // The Type Of Depth Test To Do

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)

    Sphere = gluNewQuadric()
    cylinder = gluNewQuadric()
    disk = gluNewQuadric()
    partialdisk = gluNewQuadric()

    gluQuadricNormals(Sphere, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(cylinder, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(disk, GLU_SMOOTH)  # // Create Smooth Normals

    mat_specular = [8.0, 8.0, 1.0, 0.0]
    mat_shinines = 40.0
    light_position = [120.6, 14.0, 41.0, 10.7]

    f0 = 1
    f1 = 0.5
    f2 = 0.5
    f3 = 0.5

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_BACK, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shinines)
    glMaterialfv(GL_BACK, GL_SHININESS, mat_shinines)
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

    time = 0
    rotangle = 0
    rotangle1 = 0
    rotangle2 = 0
    rotangle3 = 0
    xpos = -5
    ypos = 0
    zpos = -10


def Resize(Width, Height):
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, Width / Height, 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def timer1():
    global time, t_grph

    t_grph = []

    legs()

    time += 0.01

    t_grph += [time]


def timer2():
    global rotangle, rotangle1, rotangle2, xpos, rtgl_grph

    rtgl_grph = []

    rotangle1 = 90 * sin(2 * pi * f0 * time)
    rotangle = 90 * abs(sin(2 * pi * f1 * time))
    rotangle3 = 180 * abs(sin(2 * pi * f2 * time))
    rotangle2 = 90 * abs(sin(0.1 * time))

    xpos += 0.005 * cos(rotangle * pi / 180)

    rtgl_grph += [rotangle]


def graph():
    # fig1.clear()
    ax1 = fig1.add_subplot(111)
    ax1.set_xlabel("angle", fontsize=6)
    ax1.scatter(t_grph, rtgl_grph)
    ax1.tick_params(direction='in', labelsize=6)
    plt1_windows.draw()


def legs():
    global f0, f1, f2, f3

    inp1._setitem('from', 0)
    inp1._setitem_('to', 360)
    inp2._setitem('from', 0)
    inp2._setitem_('to', 360)
    inp3._setitem('from', 0)
    inp3._setitem_('to', 360)

    pitch = int(inp1.get())
    yaw = int(inp2.get())
    roll = int(inp3.get())

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_LIGHTING)
    glTranslate(xpos, ypos, zpos)

    glRotatef(pitch, 0.0, 0.0, 1.0)
    glRotatef(yaw, 0.0, 1.0, 0.0)
    glRotatef(roll, 1.0, 0.0, 1.0)

    panjang = 4
    panjang1 = 3

    tp = 1.25
    tl = 0.5
    tt = 0.175

    glRotate(90, 1, 0, 0)  # to result pendulum in sagittal plane, z axis rotated around x axis
    # arms
    # upper arm rotation
    glRotate(rotangle, 0, 1, 0)  # ;//sagittal plane xy  around y alias z
    glRotate(rotangle, 1, 0, 0)  # ;//frontal plane xy around x axis

    glPushMatrix()
    gluSphere(gluNewQuadric(), 1.0, 32, 32)  # joint 1 center
    gluCylinder(gluNewQuadric(), 0.65, 0.35, panjang, 32, 32)
    glTranslatef(0.0, 0.0, panjang)
    gluSphere(gluNewQuadric(), 0.5, 32, 32)  # joint 2 center
    # lower arm rotation
    glRotatef(1.5 * rotangle, 1.0, 0.0, 0.0)  # lower arm rotation around x axis yz frontal plan
    glPushMatrix()
    gluCylinder(gluNewQuadric(), 0.35, 0.25, panjang1, 32, 32)  # lower arm long cylinder
    glTranslate(0, 0, panjang1)
    # joint3 wrist joint
    glRotatef(rotangle, 1.0, 0.0, 0.0)
    gluSphere(gluNewQuadric(), 0.4, 32, 32)  # joint 3 center wrist joint
    glPushMatrix()
    gluCylinder(gluNewQuadric(), 0.55, 0.55, 0.75, 32, 32)  # hand segment
    glTranslatef(0.0, 0.0, 0.75)
    gluSphere(gluNewQuadric(), 0.55, 32, 32)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()


def main():
    pygame.display.set_mode((800, 500), DOUBLEBUF | OPENGL)
    Resize(800, 500)
    create()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        timer1()
        timer2()
        graph()

        pygame.display.flip()
        pygame.time.wait(10)
        root.update()


cvs1 = Frame(utama, padx=45, pady=10)
cvs1.pack(side=LEFT)

b1 = Frame(labelGab, padx=5, pady=10)
b1.pack(side=LEFT)

plt1_windows = FigureCanvasTkAgg(fig1, cvs1)
plt1_windows.get_tk_widget().pack()

button1 = Button(b1, text='BASIC', command=main, pady=3, padx=10)
button1.pack(pady=10)

entry = LabelFrame(labelGab, text="Angle Control", padx=25, pady=10)
entry.pack(side=LEFT)

et1 = Frame(entry, padx=10, pady=10)
et1.pack(side=LEFT)

et2 = Frame(entry, padx=10, pady=10)
et2.pack(side=LEFT)

et3 = Frame(entry, padx=10, pady=10)
et3.pack(side=LEFT)

button2 = Button(b1, text='UPPERLIMB', pady=3)
button2.pack(pady=10)

button3 = Button(b1, text='CYLINDER', pady=3)
button3.pack(pady=10)

title6 = Label(et1, text="PITCH")
title6.pack()
title7 = Label(et1, text="YAW")
title7.pack()
title8 = Label(et1, text="ROLL")
title8.pack()

var0 = IntVar()
var1 = IntVar()
var2 = IntVar()

inp1 = Spinbox(et2, from_=0, to=None, width=5, command=legs)
inp1.pack(pady=2)
inp2 = Spinbox(et2, from_=0, to=None, width=5, command=legs)
inp2.pack(pady=2)
inp3 = Spinbox(et2, from_=0, to=None, width=5, command=legs)
inp3.pack(pady=2)