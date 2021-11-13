import os
import pygame
import tkinter
from tkinter import messagebox as mb
import math as mt
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# Declaration of Additional Variable
font9 = "-family {Showcard Gothic} -size 14 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"

###input initial condition
###THIGH INISIAL
panjang_1 = 0.383
massa_1 = 6.86
a_1 = 0.42 # *panjang_1
inersia_1 = 0.133

###SHANK INISIAL
panjang_2 = 0.407
massa_2 = 2.76
a_2 = 0.41 # *panjang_2
inersia_2 = 0.048

###FOOT INISIAL
panjang_3 = 0.149
massa_3 = 0.89
a_3 = 0.4 # *panjang_3
inersia_3 = 0.004

###constant variable
t = 0.0
h = 0.1
grav = 9.8
tetadot = np.array(([0.0], [0.0], [0.0]))

###screenstatus
Status = 0

###mengubah derajat ke radian
teta_1, teta_2, teta_3 = 0, 0, 0

# Make a Tkinter Canvas
window = tkinter.Tk()
window.title("Musculoskeletal Movement")
window.geometry("+250+10")

# Declare Attribute
TitlePos = tkinter.Frame(window, width=1050, height=40, background='#e2e6e2')
TitlePos.pack()
TitlePos.pack_propagate(0)

Title = tkinter.Label(TitlePos, text="Musculoskeletal Movement", font=font9, bg='#e2e6e2')
Title.pack(pady=5, expand=tkinter.YES, side=tkinter.TOP)

MainPos = tkinter.Frame(window, width=1050, height=550, background='#e2e6e2')
MainPos.pack()
MainPos.pack_propagate(0)

MainPos1 = tkinter.Frame(MainPos, width=1050, height=400, background='#e2e6e2')
MainPos1.pack()
MainPos1.pack_propagate(0)

OpenGLPos = tkinter.LabelFrame(MainPos1, width=682, height=400, text='''OPEN GL''', background='#e2e6e2',
                               labelanchor=tkinter.N)
OpenGLPos.pack(padx=11, side=tkinter.LEFT)
OpenGLPos.pack_propagate(0)

embed = tkinter.LabelFrame(OpenGLPos, width=650, height=360, background='#e2e6e2')
embed.pack(expand=tkinter.YES)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

TombolPos = tkinter.Frame(MainPos1, width=368, height=400, background='#e2e6e2')
TombolPos.pack(padx=5, side=tkinter.LEFT)
TombolPos.pack_propagate(0)

mf1 = tkinter.LabelFrame(TombolPos, width=360, height=210, text="PARAMETER", bg="#e2e6e2")
mf1.pack()
mf1.pack_propagate(0)
mf1_help1 = tkinter.Frame(mf1, width=70, height=190, bg='#e2e6e2')
mf1_help1.pack(padx=4, side=tkinter.LEFT)
mf1_help1.pack_propagate(0)
mf1_help2 = tkinter.Frame(mf1, width=20, height=190, bg='#e2e6e2')
mf1_help2.pack(side=tkinter.LEFT)
mf1_help2.pack_propagate(0)
mf1_help3 = tkinter.Frame(mf1, width=55, height=190, bg='#e2e6e2')
mf1_help3.pack(side=tkinter.LEFT)
mf1_help3.pack_propagate(0)
mf1_help4 = tkinter.Frame(mf1, width=95, height=190, bg='#e2e6e2')
mf1_help4.pack(padx=2, side=tkinter.LEFT)
mf1_help4.pack_propagate(0)
mf1_help5 = tkinter.Frame(mf1, width=20, height=190, bg='#e2e6e2')
mf1_help5.pack(side=tkinter.LEFT)
mf1_help5.pack_propagate(0)
mf1_help6 = tkinter.Frame(mf1, width=55, height=190, bg='#e2e6e2')
mf1_help6.pack(side=tkinter.LEFT)
mf1_help6.pack_propagate(0)

mf1_entry1 = tkinter.Entry(mf1_help3, width=6)
mf1_entry1.pack(pady=11)
mf1_entry2 = tkinter.Entry(mf1_help3, width=6)
mf1_entry2.pack()
mf1_entry3 = tkinter.Entry(mf1_help3, width=6)
mf1_entry3.pack(pady=11)
mf1_entry4 = tkinter.Entry(mf1_help3, width=6)
mf1_entry4.pack()
mf1_entry5 = tkinter.Entry(mf1_help3, width=6)
mf1_entry5.pack(pady=11)
mf1_entry6 = tkinter.Entry(mf1_help3, width=6)
mf1_entry6.pack()
mf1_entry7 = tkinter.Entry(mf1_help6, width=6)
mf1_entry7.pack(pady=11)
mf1_entry8 = tkinter.Entry(mf1_help6, width=6)
mf1_entry8.pack()
mf1_entry9 = tkinter.Entry(mf1_help6, width=6)
mf1_entry9.pack(pady=11)
mf1_entry10 = tkinter.Entry(mf1_help6, width=6)
mf1_entry10.pack()
mf1_entry11 = tkinter.Entry(mf1_help6, width=6)
mf1_entry11.pack(pady=11)
mf1_entry12 = tkinter.Entry(mf1_help6, width=6)
mf1_entry12.pack()

mf1_label1_1 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Length 1 (m)", bg='#e2e6e2')
mf1_label1_1.pack(pady=9)
mf1_label1_2 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Length 2 (m)", bg='#e2e6e2')
mf1_label1_2.pack()
mf1_label1_3 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Length 3 (m)", bg='#e2e6e2')
mf1_label1_3.pack(pady=9)
mf1_label1_4 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Mass 1 (kg)", bg='#e2e6e2')
mf1_label1_4.pack()
mf1_label1_5 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Mass 2 (kg)", bg='#e2e6e2')
mf1_label1_5.pack(pady=9)
mf1_label1_6 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Mass 3 (kg)", bg='#e2e6e2')
mf1_label1_6.pack()
mf1_label1_7 = tkinter.Label(mf1_help4, anchor="w", width=13, text="CoG 1 (% Length)", bg='#e2e6e2')
mf1_label1_7.pack(pady=9)
mf1_label1_8 = tkinter.Label(mf1_help4, anchor="w", width=13, text="CoG 2 (% Length)", bg='#e2e6e2')
mf1_label1_8.pack()
mf1_label1_9 = tkinter.Label(mf1_help4, anchor="w", width=13, text="CoG 3 (% Length)", bg='#e2e6e2')
mf1_label1_9.pack(pady=9)
mf1_label1_10 = tkinter.Label(mf1_help4, anchor="w", width=13, text="Inertia 1 (kgm^2)", bg='#e2e6e2')
mf1_label1_10.pack()
mf1_label1_11 = tkinter.Label(mf1_help4, anchor="w", width=13, text="Inertia 2 (kgm^2)", bg='#e2e6e2')
mf1_label1_11.pack(pady=9)
mf1_label1_12 = tkinter.Label(mf1_help4, anchor="w", width=13, text="Inertia 3 (kgm^2)", bg='#e2e6e2')
mf1_label1_12.pack()

mf1_label2_1 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_1.pack(pady=9)
mf1_label2_2 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_2.pack()
mf1_label2_3 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_3.pack(pady=9)
mf1_label2_4 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_4.pack()
mf1_label2_5 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_5.pack(pady=9)
mf1_label2_6 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_6.pack()
mf1_label2_7 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_7.pack(pady=9)
mf1_label2_8 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_8.pack()
mf1_label2_9 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_9.pack(pady=9)
mf1_label2_10 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_10.pack()
mf1_label2_11 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_11.pack(pady=9)
mf1_label2_12 = tkinter.Label(mf1_help5, text=":", anchor="w", bg='#e2e6e2')
mf1_label2_12.pack()

mf2 = tkinter.Frame(TombolPos, width=360, height=290, background='#e2e6e2')
mf2.pack(padx=0)
mf2.pack_propagate(0)
mf2_1 = tkinter.Frame(mf2, width=90, height=290, bg="#e2e6e2")
mf2_1.pack(side=tkinter.LEFT)
mf2_1.pack_propagate(0)


def render1(teta1, teta2, teta3):
    mat_specular = [8.0, 8.0, 1.0, 0.0]
    mat_shinines = 40.0
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

    xpos = -2 / 5
    ypos = -1 / 5
    zpos = -15 / 5

    teta1_degree = (teta1 * 180) / np.pi
    teta2_degree = (teta2 * 180) / np.pi
    teta3_degree = (teta3 * 180) / np.pi

    tp = 0.130  # ; //panjang tangan
    tl = 0.1  # ; //lebar tangan
    tt = 0.0175  # ;//tebal tangan

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_LIGHTING)

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    gluSphere(gluNewQuadric(), 0.09, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(teta1_degree, 0.0, 1.0, 0.0)
    gluCylinder(gluNewQuadric(), 0.090, 0.075, panjang_1, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef(panjang_1 * mt.sin(teta1), -panjang_1 * mt.cos(teta1), 0.0)
    gluSphere(gluNewQuadric(), 0.080, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef(panjang_1 * mt.sin(teta1), -panjang_1 * mt.cos(teta1), 0.0)
    glRotatef(-teta2_degree, 0.0, 0.0, 1.0)
    glTranslatef(-panjang_1 * mt.sin(teta1), panjang_1 * mt.cos(teta1), 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(teta1_degree, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, panjang_1)
    gluCylinder(gluNewQuadric(), 0.065, 0.035, panjang_2, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1 * mt.sin(teta1) - panjang_2 * mt.sin(teta2 - teta1)),
                 -(panjang_1 * mt.cos(teta1) + panjang_2 * mt.cos(teta2 - teta1)), 0.0)
    gluSphere(gluNewQuadric(), 0.040, 32, 32)
    glPopMatrix()

    glPushMatrix()
    Pendataran = mt.atan(0.025 / (panjang_3 * 5))
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1 * mt.sin(teta1) - panjang_2 * mt.sin(teta2 - teta1)),
                 -(panjang_1 * mt.cos(teta1) + panjang_2 * mt.cos(teta2 - teta1)), 0.0)
    glRotatef(90 - (teta2_degree - teta1_degree + teta3_degree + ((Pendataran * 180) / np.pi)), 0.0, 0.0, 1.0)
    glTranslatef(-(panjang_1 * mt.sin(teta1) - panjang_2 * mt.sin(teta2 - teta1)),
                 (panjang_1 * mt.cos(teta1) + panjang_2 * mt.cos(teta2 - teta1)), 0.0)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -(panjang_1 * mt.cos(teta1) + panjang_2 * mt.cos(teta2 - teta1)),
                 (panjang_1 * mt.sin(teta1) - panjang_2 * mt.sin(teta2 - teta1)))

    # hand
    glRotate(-180, 1, 0, 0)  # ;
    glRotate(-45, 0, 0, 1)  # ;
    # // gldisable(gl_lighting);
    glBegin(GL_POLYGON)  # ; //awal poligon  atap
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;   //posisi dalam x y z  +tt
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glEnd()  # ;              //akhir poligon

    glBegin(GL_POLYGON)  # ;     //dasar -tt
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //samping kiri -t1
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //samping kanan +tl
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;    //depan sumbu z +tp
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //belakang sumbu z 0
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glEnd()

    # {first segment}
    # {centre fingers}
    jarip = 0.025  # ;
    jarip1 = 0.023  # ;
    jarip2 = 0.027  # ;
    glTranslate(0, 0, tp)  # ; {ref} //pindahkan referensi koordinat
    glRotate(360, 1, 0, 0)  # ;   {rotation1}
    glEnable(GL_LIGHTING)  # ;
    gluCylinder(gluNewQuadric(), 0.0080, 0.0075, jarip, 32, 10)  # ;    //jari tengan dengan panjang jarip
    gluSphere(gluNewQuadric(), 0.0080, 32, 32)  # ; //sendi

    # {pointer finger}
    jarispace = 0.05  # ;
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;

    # {tumb}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;

    # {jari manis}
    glTranslate(-3 * jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {kelingking}
    glTranslate(-jarispace, 0, 0)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip, 32, 10)  # ;

    # {second segment}
    # {kelingking}
    glTranslate(0, 0, jarip)  # ; {ref}
    glRotate(10, 1, 0, 0)  # ;   {rotation1}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    glTranslate(0, 0, jarip1)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    glTranslate(0, 0, -jarip1)  # ; {ref}

    # {jari manis}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 32)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {jari tengah}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {jari telunjuk}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;

    # {tumb}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    # //jarip1:=0.15;
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;
    glTranslate(0, 0, jarip1)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;

    # {third segment}

    # {telunjuk}
    glTranslate(-jarispace, 0, 0)  # ; {ref}
    glRotate(10, 1, 0, 0)  # ;   {rotation1}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;

    # {jaritengah}
    glTranslate(-jarispace, 0, -jarip2)  # ; {ref}
    glPushMatrix()  # ;
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;

    # {jari manis}
    glTranslate(-jarispace, 0, -jarip2)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;
    glPopMatrix()
    glPopMatrix()


def chart(iteration, hip, knee, ankle):
    global ax1, ax2, ax3

    ax1.plot(np.arange(iteration + 1), hip)
    ax2.plot(np.arange(iteration + 1), knee)
    ax3.plot(np.arange(iteration + 1), ankle)


def Start():
    global Status

    Status = 1
    pass


def Stop():
    global Status

    Status = 2
    pass


def Clear():
    global wqt, Status, teta_1, teta_2, teta_3, ttn_1, ttn_2, ttn_3

    wqt, Status, teta_1, teta_2, teta_3 = 0, 0, 0, 0, 0
    ttn_1, ttn_2, ttn_3 = [], [], []
    ax1.clearfig()
    ax2.clearfig()
    ax3.clearfig()
    pass


def About():
    mb.showinfo("About", "ECG Synthetic Generator by Dzikrur Rohmani Z R M H.\n\nBiomedical Engineering Department\nInstitut Teknologi \
Sepuluh Nopember (ITS) Surabaya")


def Close():
    global Running

    Running = False

# COMMAND
mf2_1_button1 = tkinter.Button(mf2_1, width=15, text="START", command=Start)
mf2_1_button1.pack(pady=5)
mf2_1_button2 = tkinter.Button(mf2_1, width=15, text="STOP", command=Stop)
mf2_1_button2.pack()
mf2_1_button3 = tkinter.Button(mf2_1, width=15, text="CLEAR", command=Clear)
mf2_1_button3.pack(pady=5)
mf2_1_button4 = tkinter.Button(mf2_1, width=15, text="ABOUT", command=About)
mf2_1_button4.pack()
mf2_1_button4 = tkinter.Button(mf2_1, width=15, text="CLOSE", command=Close)
mf2_1_button4.pack(pady=5)

# if __name__ == "__main__":
#     ###mengubah derajat ke radian
#     wqt = 0
#     Scale = 0

#     pygame.init()
#     display = (800, 600)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     glClearColor(0.9, 0., 0.9, 0.1)
#     glViewport(0, 0, display[0], display[1])
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(50.0, display[0] / display[1], 1, 100.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

#     Running = True
#     while Running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 Running = False
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         render1(teta_1, teta_2, teta_3)
#         pygame.display.flip()
#         pygame.time.wait(1)
#         teta_1 += 0.1
#         try:
#             window.update()
#         except tkinter.TclError:
#             Running = False
#     pygame.quit()
