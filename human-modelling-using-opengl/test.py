"""This module contains all of the necessary PyGame components for
running a simplified game loop.
Use it for test cases on PyGame-related code.
"""
import sys
import pygame
from pygame.locals import *
from tkinter import *
import math as mt
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
# Import additional modules here.


# Feel free to edit these constants to suit your requirements.
FRAME_RATE = 60.0
SCREEN_SIZE = (640, 480)

###constant variable
grav = 9.8
tetadot = np.array(([0.0], [0.0]))

###input initial condition
###UPPERARM INISIAL
panjang_1 = 0.383  # upper arm length
massa_1 = (0.022 * (73 * grav) + 4.76) / grav  # upper arm
a_1 = 0.507

###FOREARM INISIAL
panjang_2 = 0.517  # lower arm length
massa_2 = (0.013 * (73 * grav) + 2.41) / grav  # forearm
a_2 = 0.417

###HAND INISIAL
panjang_3 = 0.130  # hand
massa_3 = (0.005 * (73 * grav) + 0.75) / grav  # hand
a_3 = 0.515

###single pendulum approach
panjang_t = panjang_1 + panjang_2 + panjang_3
massa_t = massa_1 + massa_2 + massa_3
pusat_m = ((massa_1 * a_1 * panjang_1) + (massa_2 * (a_2 * panjang_2 + panjang_1)) + (
            massa_3 * (a_3 * panjang_3 + panjang_2 + panjang_1))) / massa_t
a_t = pusat_m / panjang_t

###INIT
Status = 0
t = 0.0
h = 0.05
teta_1, teta_2 = 0, 0
wqt = 0

ttn_1, ttn_2 = [], []

tau1 = [10]
tau2 = [0.5]

reftheta, refphi = [], []
theta, phi = [], []

RMSE = 0
ebef_theta, ebef_phi = 0, 0
sum_jum_theta, sum_jum_phi = 0, 0
err_theta, err_phi = [0], [0]

###INIT
Status = 0
t = 0.0
h = 0.001
wqt = 0

tau1 = [10]
tau2 = [0.5]

ttn = 0
ppn = 0

reftheta, refphi = [], []
theta, phi = [], []

RMSE = 0
ebef_theta, ebef_phi = 0, 0
sum_jum_theta, sum_jum_phi = 0, 0
err_theta, err_phi = [0], [0]



def inverse(x):
    M_invers = np.zeros([2, 2])
    I = np.identity(2)
    y = np.zeros([4, 4])

    for a in range(2):
        for b in range(2):
            y[a][b] = x[a][b]
            y[a][b + 2] = I[a][b]
    for a in range(2):
        for b in range(4):
            if b != a:
                c = y[b][a] / y[a][a]
                for d in range(4):
                    y[b][d] = y[b][d] - c * y[a][d]
    for a in range(2):
        c = y[a][a]
        for b in range(4):
            y[a][b] = y[a][b] / c
    for a in range(2):
        for b in range(2):
            M_invers[a][b] = y[a][b + 2]

    return M_invers


def function(teta_1, teta_2, tetadot1, tetadot2):
    tetadotdot1 = (tau1[-1] - (massa_t * panjang_t ** 2 * tetadot1) / 3 - massa_t * grav * a_t * panjang_t * mt.cos(
        teta_2) * mt.sin(teta_1) + massa_t * a_t ** 2 * panjang_t ** 2 * tetadot2 * mt.sin(2 * teta_2) * tetadot1) / (
                              massa_t * a_t ** 2 * panjang_t ** 2 * mt.cos(teta_2) ** 2)
    tetadotdot2 = (tau2[-1] - (massa_t * panjang_t ** 2 * a_t ** 2 * mt.sin(
        2 * teta_2) * tetadot1 ** 2) / 2 - massa_t * grav * a_t * panjang_t * mt.cos(teta_1) * mt.sin(teta_2)) / (
                              massa_t * panjang_t ** 2 * a_t ** 2 + (massa_t * panjang_t ** 2) / 3)

    return [tetadotdot1, tetadotdot2]


def runge_kutta(t_1, t_2, ttd_1, ttd_2):
    k_1 = np.zeros([2, 1])
    k_2 = np.zeros([2, 1])
    k_3 = np.zeros([2, 1])
    k_4 = np.zeros([2, 1])

    tetadotdot = function(t_1, t_2, ttd_1, ttd_2)
    k_1[0] = (h / 2) * tetadotdot[0]
    k_1[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + (k_1[0] / 2))) / 2, t_2 + (h * (ttd_2 + (k_1[1] / 2))) / 2,
                          ttd_1 + k_1[0], ttd_2 + k_1[1])
    k_2[0] = (h / 2) * tetadotdot[0]
    k_2[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + (k_1[0] / 2))) / 2, t_2 + (h * (ttd_2 + (k_1[1] / 2))) / 2,
                          ttd_1 + k_2[0], ttd_2 + k_2[1])
    k_3[0] = (h / 2) * tetadotdot[0]
    k_3[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + k_3[0])), t_2 + (h * (ttd_2 + k_3[1])), ttd_1 + (2 * k_3[0]),
                          ttd_2 + (2 * k_3[1]))
    k_4[0] = (h / 2) * tetadotdot[0]
    k_4[1] = (h / 2) * tetadotdot[1]

    tetadot1_n = ttd_1 + (k_1[0] + 2 * k_2[0] + 2 * k_3[0] + k_4[0]) / 3
    tetadot2_n = ttd_2 + (k_1[1] + 2 * k_2[1] + 2 * k_3[1] + k_4[1]) / 3

    teta1_n = t_1 + h * (tetadot1_n + ((k_1[0] + k_2[0] + k_3[0]) / 3))
    teta2_n = t_2 + h * (tetadot2_n + ((k_1[1] + k_2[1] + k_3[1]) / 3))

    return teta1_n, teta2_n, tetadot1_n, tetadot2_n


def glWin():
    # SetupPixelFormat
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glShadeModel(GL_SMOOTH)  # // Enables Smooth Color Shading
    glClearDepth(1.0)  # // Depth Buffer Setup
    glEnable(GL_DEPTH_TEST)  # // Enable Depth Buffer
    glDepthFunc(GL_LESS)  # // The Type Of Depth Test To Do

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)

    Sphere = gluNewQuadric()
    cylinder = gluNewQuadric()
    disk = gluNewQuadric()

    gluQuadricNormals(Sphere, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(cylinder, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(disk, GLU_SMOOTH)  # // Create Smooth Normals

    mat_specular = [8.0, 8.0, 1.0, 0.0]
    mat_shinines = 40.0
    light_position = [120.6, 14.0, 41.0, 10.7]

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


def render1(teta1, teta2):
    teta1_draw = teta1-(np.pi/2)
    teta2_draw = teta2+(np.pi/2)

    glLoadIdentity()
    glEnable(GL_LIGHTING)

    xpos = -2 / 5
    ypos = -0 / 5
    zpos = -15 / 5

    teta1_degree = (teta1 * 180) / np.pi
    teta2_degree = (teta2 * 180) / np.pi
    teta1_dedraw = (teta1_draw * 180) / np.pi
    teta2_dedraw = (teta2_draw * 180) / np.pi

    tp = 0.130  # ; //panjang tangan
    tl = 0.1  # ; //lebar tangan
    tt = 0.0175  # ;//tebal tangan

    # print(panjang_1 * mt.cos(teta1_draw) * mt.sin(teta2_draw), panjang_1 * mt.sin(teta1) * mt.cos(teta2))
    # print(panjang_1 * mt.sin(teta1_draw) * mt.sin(teta2_draw), -panjang_1 * mt.cos(teta1) * mt.cos(teta2))
    # print(panjang_1 * mt.cos(teta2_draw), -panjang_1 * mt.sin(teta2))

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    gluSphere(gluNewQuadric(), 0.09, 32, 32)
    glPopMatrix()

    h1 = 0 #5
    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glRotatef(teta1_dedraw-h1, 0.0, 0.0, 1.0)
    glRotatef(teta2_dedraw-h1, 0.0, 1.0, 0.0)
    gluCylinder(gluNewQuadric(), 0.080, 0.060, panjang_1, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef(panjang_1 * mt.cos(teta1_draw-(h1*np.pi/180)) * mt.sin(teta2_draw-(h1*np.pi/180)),
                 panjang_1 * mt.sin(teta1_draw-(h1*np.pi/180)) * mt.sin(teta2_draw-(h1*np.pi/180)),
                 panjang_1 * mt.cos(teta2_draw-(h1*np.pi/180)))
    gluSphere(gluNewQuadric(), 0.080, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glRotatef(teta1_dedraw, 0.0, 0.0, 1.0)
    glRotatef(teta2_dedraw, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, panjang_1)
    gluCylinder(gluNewQuadric(), 0.065, 0.035, panjang_2, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1+panjang_2) * mt.cos(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.sin(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.cos(teta2_draw))
    gluSphere(gluNewQuadric(), 0.040, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1+panjang_2) * mt.cos(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.sin(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.cos(teta2_draw))
    # glRotatef(-teta3*180/np.pi, 0.0, 1.0, 0.0)
    glRotatef(teta1_degree, 0.0, 0.0, 1.0)
    glRotatef(teta2_degree, 1.0, 0.0, 0.0)
    glRotatef(-45, 0.0, 1.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)

    # hand
    glRotate(-180, 1, 0, 0)  # ;
    glRotate(-45, 0, 0, 1)  # ;
    # // gldisable(gl_lighting);
    glEnable(GL_LIGHTING)  # ;
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
    # glEnable(GL_LIGHTING)  # ;
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
    

def pygame_modules_have_loaded():
    success = True

    if not pygame.display.get_init:
        success = False
    if not pygame.font.get_init():
        success = False
    if not pygame.mixer.get_init():
        success = False

    return success

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()

if pygame_modules_have_loaded():
    game_screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Test')
    clock = pygame.time.Clock()

    def declare_globals():
        # The class(es) that will be tested should be declared and initialized
        # here with the global keyword.
        # Yes, globals are evil, but for a confined test script they will make
        # everything much easier. This way, you can access the class(es) from
        # all three of the methods provided below.
        global Status, t, h, teta_1, teta_2, ttn_1, ttn_2, wqt, tau1, tau2, reftheta, refphi, theta, phi, RMSE, \
        ebef_theta, ebef_phi, sum_jum_theta, sum_jum_phi, err_theta, err_phi
        
        global render1, glWin, runge_kutta, function, inverse
        

    def prepare_test():
        # Add in any code that needs to be run before the game loop starts.
        glClearColor(0., 0.69, 0.69, 0.2)
        glViewport(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50.0, SCREEN_SIZE[0] / SCREEN_SIZE[1], 1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
            

    def handle_input(key_name):
        # Add in code for input handling.
        # key_name provides the String name of the key that was pressed.
        pass

    def update(screen, time):
        # Add in code to be run during each update cycle.
        # screen provides the PyGame Surface for the game window.
        # time provides the seconds elapsed since the last update.
        global Status, t, h, teta_1, teta_2, ttn_1, ttn_2, wqt, tau1, tau2, reftheta, refphi, theta, phi, RMSE, \
        ebef_theta, ebef_phi, sum_jum_theta, sum_jum_phi, err_theta, err_phi, ttn, ppn
        
        global render1, glWin, runge_kutta, function, inverse
        
        glWin()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        render1(ttn, ppn)
        
        v1 = 0.5 * (err_theta[-1]**2)
        v2 = 0.5 * (err_phi[-1]**2)
        try:
            gradien1 = v1 * theta[-1] * (1 - theta[-1])
            gradien2 = v2 * phi[-1] * (1 - phi[-1])
        except:
            gradien1 = v1 * ttn * (1 - ttn)
            gradien2 = v2 * ppn * (1 - ppn)
        tau1 += [tau1[-1] - (0.9 * gradien1)]
        tau2 += [tau2[-1] - (0.9 * gradien2)]
        reftheta += [np.exp(-2 * t) * np.cos(10 * np.pi * t)]
        refphi += [0]
        theta_n, phi_n, thetadot_n, phidot_n = runge_kutta(ttn, ppn, tetadot[0], tetadot[1])
        tetadot[0] = thetadot_n
        tetadot[1] = phidot_n
        theta += [theta_n]
        phi += [phi_n]
        ttn = theta_n
        ppn = phi_n
        err_theta += [(reftheta[-1] - theta[-1])]
        err_phi += [(refphi[-1] - phi[-1])]
        RMSE += err_theta[-1] ** 2
        RMSE += err_phi[-1] ** 2
        RMSE /= 2
        wqt = wqt + 1
        t += h
        
        pygame.display.update()

    # Add additional methods here.

    def main():
        declare_globals()
        prepare_test()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    handle_input(key_name)

            milliseconds = clock.tick(FRAME_RATE)
            seconds = milliseconds / 1000.0
            update(game_screen, seconds)

            sleep_time = (1000.0 / FRAME_RATE) - milliseconds
            if sleep_time > 0.0:
                pygame.time.wait(int(sleep_time))
            else:
                pygame.time.wait(1)

    main()