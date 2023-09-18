# Treba vsetky kocky posunut o 0.5 do lava
# neviem co ale daco so suradnicami je strasne dojebane

import sys, time, threading
from math import sin, cos
from random import randint
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#angle of rotation
xpos= 2
ypos= 0
zpos= 3
xrot= 0
yrot= 90
angle= lastx= lasty = 0

frame_count = 0
start_time = 0

window_height = 1500
window_width = 3000

initial_mouse_position = (window_width // 2, window_height // 2)

platform_x = 10
platform_z = 10

bludisko_2d = [
["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"], 
["#", "#", " ", " ", " ", "#", " ", " ", " ", "#", "#"],
[" ", " ", " ", "#", " ", "#", " ", "#"," " , "#", "#"],
["#", "#", "#", "#", " ", " ", " ", "#", " ", "#", "#"],
["#", "#", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
["#", "#", "#", " ", " ", " ", "#", "#", "#", " ", "#"],
["#", "#", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
["#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#"],
["#", "#", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
["#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"]
]

def init():
    global positionz, positionx
    glEnable(GL_DEPTH_TEST) #enable the depth testing
    glEnable(GL_LIGHTING) #enable the lighting
    glEnable(GL_LIGHT0) #enable LIGHT0, our Diffuse Light
    glShadeModel(GL_SMOOTH) #set the shader to smooth shader
    
def camera():
    global xrot, yrot, xpos, ypos, zpos
    glRotatef(xrot,1.0,0.0,0.0)  #rotate our camera on teh x-axis (left and right)
    glRotatef(yrot,0.0,1.0,0.0)  #rotate our camera on the y-axis (up and down)
    glTranslated(-xpos,-ypos,-zpos) #translate the screen to the position of our camera

def display():
    global angle, frame_count, start_time, bludisko_2d, xpos, ypos, zpos
    glClearColor(0.0,0.0,0.0,1.0) #clear the screen to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clear the color buffer and the depth buffer
    glLoadIdentity()
    camera()
    for x in range(platform_x):
        glPushMatrix()
        glTranslated(2, -4, x * 2 - 1) #translate the cube 
        glutSolidCube(2) #draw the cube
        for i in range(platform_z):
            glTranslated(2, 0, 0) #translate the cube
            glutSolidCube(2) #draw the cube
        glPopMatrix()

    for x in range(platform_x):
        glPushMatrix()
        glTranslated(2, 2, x * 2 - 1) #translate the cube 
        glutSolidCube(2) #draw the cube
        for i in range(platform_z):
            glTranslated(2, 0, 0) #translate the cube
            glutSolidCube(2) #draw the cube
        glPopMatrix()
    #render_text(20, window_height - 30, f"FPS: {calculate_fps():.2f}")

    for i in range(len(bludisko_2d)):
        glPushMatrix()
        glTranslated(0, -2, i * 2 - 1) #translate the cube 
        for j in range(len(bludisko_2d[i])):
            if bludisko_2d[i][j] == "#":
                glTranslated(2, 0, 0) #translate the cube
                glutSolidCube(2) #draw the cube
            else:
                glTranslated(2, 0, 0) #translate the cube
        glPopMatrix()

    for i in range(len(bludisko_2d)):
        glPushMatrix()
        glTranslated(0, 0, i * 2 - 1) #translate the cube 
        for j in range(len(bludisko_2d[i])):
            if bludisko_2d[i][j] == "#":
                glTranslated(2, 0, 0) #translate the cube
                glutSolidCube(2) #draw the cube
            else:
                glTranslated(2, 0, 0) #translate the cube
        glPopMatrix()

    glutSwapBuffers() #swap the buffers
    frame_count += 1
    angle += angle #increase the angle

def reshape(w, h):
    glViewport(0, 0, w, h); #set the viewport to the current window specifications
    glMatrixMode(GL_PROJECTION); #set the matrix to projection

    glLoadIdentity()
    gluPerspective(90, w / h, 0.1, 200.0)
    #set the perspective (angle of sight, width, height, , depth)
    glMatrixMode(GL_MODELVIEW); #set the matrix back to model

def glkeyboard (key, x, y):
    global xrot, xpos, ypos, zpos, xrot, yrot, angle, lastx, lasty, positionz, positionx
    if (key==b'y'):
        xrot += 1
        if (xrot >360):
            xrot -= 360
    if (key==b'q'):
        xrot -= 1
        if (xrot < -360):
            xrot += 360
    if (key==b'r'):
        yrot += 1
        if (yrot >360):
            yrot -= 360
    if (key==b'e'):
        yrot -= 1
        if (yrot < -360):
            yrot += 360
    if (key==b'w'):
        yrotrad = (yrot / 180 * 3.141592654)
        xrotrad = (xrot / 180 * 3.141592654)
        xpos += float(sin(yrotrad)) * 0.2
        zpos -= float(cos(yrotrad)) * 0.2
        #ypos -= float(sin(xrotrad))
    if (key==b's'):
        yrotrad = (yrot / 180 * 3.141592654)
        xrotrad = (xrot / 180 * 3.141592654)
        xpos -= float(sin(yrotrad)) * 0.2
        zpos += float(cos(yrotrad)) * 0.2
        #ypos += float(sin(xrotrad))
    if (key==b'd'):
        yrotrad = (yrot / 180 * 3.141592654)
        xpos += float(cos(yrotrad)) * 0.2
        zpos += float(sin(yrotrad)) * 0.2
    if (key==b'a'):
        yrotrad = (yrot / 180 * 3.141592654)
        xpos -= float(cos(yrotrad)) * 0.2
        zpos -= float(sin(yrotrad)) * 0.2
    if (key==b'k'):
        ypos += 1
    if (key==b'm'):
        ypos -= 1
    if (key==27):
        sys.exit(0)

def mouseMovement(x, y):
    global lastx, lasty, xrot, yrot, initial_mouse_position
    diffx=x-initial_mouse_position[0] #check the difference between the current x and the last x position
    diffy=y-initial_mouse_position[1] #check the difference between the current y and the last y position
    lastx=x #set lastx to the current x position
    lasty=y #set lasty to the current y position
    if xrot + float(diffy / 20) < 90 and xrot + float(diffy / 20) > -90:
        xrot += float(diffy / 20) #set the xrot to xrot with the addition of the difference in the y position
    yrot += float(diffx / 20) #set the xrot to yrot with the addition of the difference in the x position

def handle_visibility(visibility):
    if visibility == GLUT_VISIBLE:
        glutSetCursor(GLUT_CURSOR_NONE)
    else:
        glutSetCursor(GLUT_CURSOR_INHERIT)

def snap_pointer_to_center():   
    while True:
        glutWarpPointer(window_width // 2, window_height // 2)
        time.sleep(0.2)

def start_snapping_thread():
    threading.Thread(target=snap_pointer_to_center).start()

def render_text(x, y, text):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(x, y, 0.0)

    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(0.0, 0.0)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))

    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def calculate_fps():
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > 0:
        fps = frame_count / elapsed_time
        return fps
    return 0.0


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition (100, 100)
glutCreateWindow("A basic OpenGL Window")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutPassiveMotionFunc(mouseMovement)
start_snapping_thread()

start_time = time.time()

glutVisibilityFunc(handle_visibility)

#check for mouse movement
glutKeyboardFunc(glkeyboard)
glutMainLoop()
