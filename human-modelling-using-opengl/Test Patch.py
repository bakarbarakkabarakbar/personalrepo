def render2(teta1, teta2, teta3, theta1_dot, theta2_dot, theta3_dot):
    global f0, f1, f2, f3, rotangle3, pitch, yaw, roll
    global iners1, iners2, iners3
    # inp1._setitem('from', -360)
    # inp1._setitem_('to', 360)
    # inp2._setitem('from', -360)
    # inp2._setitem_('to', 360)
    # inp3._setitem('from', -360)
    # inp3._setitem_('to', 360)
    pitch = 10  # int(inp1.get())
    yaw = 10  # int(inp2.get())
    roll = 10  # int(inp3.get())

    tp = 0.130  # ; //panjang tangan
    tl = 0.1  # ; //lebar tangan
    tt = 0.0175  # ;//tebal tangan

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_LIGHTING)
    teta1_degree = (teta1 * 180) / pi
    teta2_degree = (teta2 * 180) / pi
    teta3_degree = (teta3 * 180) / pi

    glTranslatef(xpos, ypos, zpos)

    glRotate(90, 1, 0, 0)  # to result pendulum in sagittal plane, z axis rotated around x axis
    glRotate(teta1_degree, 1, 0, 0)  # ganti jadi teta
    glRotate(teta1_degree, 0, 1, 0)  # ;//sagittal plane xy  around y alias z

    glPushMatrix()

    gluSphere(gluNewQuadric(), 0.09, 32, 32)
    gluCylinder(gluNewQuadric(), 0.090, 0.075, panjang1, 32, 32)
    glTranslatef(0.0, 0.0, panjang1)
    gluSphere(gluNewQuadric(), 0.080, 32, 32)
    glRotatef(-teta2_degree, 0.0, 1.0, 0.0)  # lower arm rotation around x axis yz frontal plan

    glPushMatrix()

    gluCylinder(gluNewQuadric(), 0.065, 0.035, panjang2, 32, 32)
    glTranslate(0, 0, panjang2)
    glRotatef(teta2_degree, 0.0, 1.0, 0.0)
    gluSphere(gluNewQuadric(), 0.040, 32, 32)

    # hand
    glRotate(teta1_degree, 1, 0, 0)  # ;
    # glRotate(teta1_degree,0,0,1)#;
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
    glRotate(teta2_degree, 1, 0, 0)  # ;   {rotation1}
    glEnable(GL_LIGHTING)  # ;
    glPushMatrix()  # ;
    gluCylinder(gluNewQuadric(), 0.0080, 0.0075, jarip, 32, 10)  # ;    //jari tengan dengan panjang jarip
    gluSphere(gluNewQuadric(), 0.0080, 32, 32)  # ; //sendi

    # {pointer finger}
    glPushMatrix()  # ;

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
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip, 32, 10)  #

    # {second segment}
    # {kelingking}
    glTranslate(0, 0, jarip)  # ; {ref}
    glRotate(teta3_degree, 1, 0, 0)  # ;   {rotation1}

    glPushMatrix()  # ;
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
    glRotate(teta3_degree, 1, 0, 0)  # ;   {rotation1}
    glPushMatrix()  # ;
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
    glPushMatrix()  # ;
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;

    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

    glEnd