import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (1500, 1000)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0,-40)

def draw_cube(x, y, z, color):
    vertices = (
        (x+1, y-1, z-1),
        (x+1, y+1, z-1),
        (x-1, y+1, z-1),
        (x-1, y-1, z-1),
        (x+1, y-1, z+1),
        (x+1, y+1, z+1),
        (x-1, y-1, z+1),
        (x-1, y+1, z+1)
    )
    edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
    )
    surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
    )

    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3f(*color)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        glColor3f(1,1,1)
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 0, 1, 0) # rotate the cubes around their axis
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    draw_cube(0, 0, 0, (1, 0, 0))

    draw_cube(2, 0, 0, (1, 0, 0))
    draw_cube(0, 2, 0, (1, 0, 0))
    draw_cube(-2, 0, 0, (1, 0, 0))
    draw_cube(0, -2, 0, (1, 0, 0))

    # draw_cube(4, 0, 0, (1, 0, 0))
    # draw_cube(0, 4, 0, (1, 0, 0))
    # draw_cube(-4, 0, 0, (1, 0, 0))
    # draw_cube(0, -4, 0, (1, 0, 0))

    # draw_cube(4, 2, 0, (1, 0, 0))
    # draw_cube(4, 4, 0, (1, 0, 0))

    # draw_cube(4, -4, 0, (1, 0, 0))
    # draw_cube(2, -4, 0, (1, 0, 0))

    # draw_cube(-4, -2, 0, (1, 0, 0))
    # draw_cube(-4, -4, 0, (1, 0, 0))

    # draw_cube(-2, 4, 0, (1, 0, 0))
    # draw_cube(-4, 4, 0, (1, 0, 0))
    # glClearColor(1, 1, 1, 1)
    # draw_cube(0, 0, 0, (1, 0, 0))
    # draw_cube(2, 2, 0, (1, 0, 0))
    # draw_cube(0, 2, 0, (1, 0, 0))
    # draw_cube(2, 0, 0, (1, 0, 0))
    # draw_cube(-2, 0, 0, (1, 0, 0))
    # draw_cube(0, -2, 0, (1, 0, 0))
    # draw_cube(-2, -2, 0, (1, 0, 0))
    # draw_cube(2, -2, 0, (1, 0, 0))
    # draw_cube(-2, 2, 0, (1, 0, 0))
    # draw_cube(4, 0, 0, (1, 0, 0))
    # draw_cube(0, -4, 0, (1, 0, 0))
    # draw_cube(-4, 0, 0, (1, 0, 0))
    # draw_cube(4, 2, 0, (1, 0, 0))
    # draw_cube(-4, 2, 0, (1, 0, 0))
    # draw_cube(4, 4, 0, (1, 0, 0))
    # draw_cube(-4, 4, 0, (1, 0, 0))
    # draw_cube(2, 4, 0, (1, 0, 0))
    # draw_cube(-2, 4, 0, (1, 0, 0))
    # draw_cube(6, 2, 0, (1, 0, 0))
    # draw_cube(-6, 2, 0, (1, 0, 0))
    # draw_cube(0, -6, 0, (1, 0, 0))
    # draw_cube(2, -4, 0, (1, 0, 0))
    # draw_cube(-2, -4, 0, (1, 0, 0))
    # draw_cube(-4, -2, 0, (1, 0, 0))
    # draw_cube(4, -2, 0, (1, 0, 0))
    # draw_cube(6, 0, 0, (1, 0, 0))
    # draw_cube(-6, 0, 0, (1, 0, 0))

    pygame.display.flip()
    pygame.time.wait(10)
