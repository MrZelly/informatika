import time
import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Rotation angles
angle = 0.0
angle_step = 0.5

line_width = 5.0

frame_count = 0
start_time = 0

cube_positions = [
    (0.0, 0.0, -2.0),
    (0.0, 0.0, 2.0),
    (0.0, 2.0, 0.0),
    (0.0, -2.0, 0.0),
    (0.0, -2.0, -2.0),
    (0.0, 2.0, 2.0),
    (0.0, -2.0, 2.0),
    (0.0, 2.0, -2.0),
    (2.0, 0.0, 0.0),
    (2.0, 0.0, -2.0),
    (2.0, 0.0, 2.0),
    (2.0, 2.0, 0.0),
    (2.0, -2.0, 0.0),
    (2.0, -2.0, -2.0),
    (2.0, 2.0, 2.0),
    (2.0, -2.0, 2.0),
    (2.0, 2.0, -2.0),
    (-2.0, 0.0, 0.0),
    (-2.0, 0.0, -2.0),
    (-2.0, 0.0, 2.0),
    (-2.0, 2.0, 0.0),
    (-2.0, -2.0, 0.0),
    (-2.0, -2.0, -2.0),
    (-2.0, 2.0, 2.0),
    (-2.0, -2.0, 2.0),
    (-2.0, 2.0, -2.0),
]


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def draw_cube(x, y, z):
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    colors = (
        (0, 0, 1),
        (1, 0.5, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
        (1, 1, 0)
    )
    
    edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (6, 3),
    (6, 7),
    (7, 5),
    (0, 4),
    (1, 5),
    (2, 7),
    (6, 4)
    )

    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(line_width)
    glPushMatrix()
    glTranslatef(x, y, z)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for face, color in zip(faces, colors):
        glColor3fv(color)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glPopMatrix()

def display():
    global angle, frame_count, start_time

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, -25, 0, 0, 0, 0, 1, 0)

    glRotatef(angle, 0, 1, 0)

    for position in cube_positions:
        x, y, z = position
        if isVisible(x, y, z):
            draw_cube(x, y, z)

    render_text(20, HEIGHT - 30, f"FPS: {calculate_fps():.2f}")

    glutSwapBuffers()
    frame_count += 1
    angle += angle_step

def render_text(x, y, text):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glTranslatef(x, y, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glRasterPos2f(0.0, 0.0)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def calculate_fps():
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > 0:
        fps = frame_count / elapsed_time
    return fps
    return 0.0

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def isVisible(x, y, z):
    model = glGetDoublev(GL_MODELVIEW_MATRIX)
    proj = glGetDoublev(GL_PROJECTION_MATRIX)
    view = glGetIntegerv(GL_VIEWPORT)

    clip_space_coords = gluProject(x, y, z, model, proj, view)

    x_clip, y_clip, z_clip = clip_space_coords
    ndc_x = 2.0 * (x_clip - view[0]) / view[2] - 1.0
    ndc_y = 2.0 * (y_clip - view[1]) / view[3] - 1.0

    near_plane = -proj[3][2] / (proj[2][2] - 1.0)
    far_plane = -proj[3][2] / (proj[2][2] + 1.0)

    return -1.0 <= ndc_x <= 1.0 and -1.0 <= ndc_y <= 1.0 and near_plane <= z_clip <= far_plane

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(b"OpenGL 3D Engine")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)

    init()

    global start_time
    start_time = time.time()

    glutMainLoop()

if __name__ == "__main__":
    main()


