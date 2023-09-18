import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi

# Window dimensions
width, height = 800, 600

# Maze dimensions
maze_width, maze_height = 10, 10
cell_size = 2.0

# Player position and movement speed
player_x, player_y = 1.5, 1.5
player_angle = 0.0
player_speed = 0.1

# Maze data (1s represent walls, 0s represent empty cells)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def draw_wall(x, y):
    glBegin(GL_QUADS)
    glVertex3f(x, y, 0)
    glVertex3f(x + cell_size, y, 0)
    glVertex3f(x + cell_size, y + cell_size, 0)
    glVertex3f(x, y + cell_size, 0)
    glEnd()

def draw_maze():
    for i in range(maze_height):
        for j in range(maze_width):
            if maze[i][j] == 1:
                draw_wall(j * cell_size, i * cell_size)

def handle_collision(x, y):
    cell_x = int(x // cell_size)
    cell_y = int(y // cell_size)
    if maze[cell_y][cell_x] == 1:
        return True
    return False

def update(dt):
    global player_x, player_y

    # Move forward
    if keys[b'w']:
        new_x = player_x + player_speed * cos(player_angle)
        new_y = player_y + player_speed * sin(player_angle)
        if not handle_collision(new_x, new_y):
            player_x = new_x
            player_y = new_y

    # Move backward
    if keys[b's']:
        new_x = player_x - player_speed * cos(player_angle)
        new_y = player_y - player_speed * sin(player_angle)
        if not handle_collision(new_x, new_y):
            player_x = new_x
            player_y = new_y

    # Strafe left
    if keys[b'a']:
        new_x = player_x + player_speed * sin(player_angle)
        new_y = player_y - player_speed * cos(player_angle)
        if not handle_collision(new_x, new_y):
            player_x = new_x
            player_y = new_y

    # Strafe right
    if keys[b'd']:
        new_x = player_x - player_speed * sin(player_angle)
        new_y = player_y + player_speed * cos(player_angle)
        if not handle_collision(new_x, new_y):
            player_x = new_x
            player_y = new_y

    glutTimerFunc(16, update, 0)
    glutPostRedisplay()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Set camera position and orientation
    gluLookAt(player_x, player_y, 1.0,
              player_x + cos(player_angle), player_y + sin(player_angle), 1.0,
              0.0, 0.0, 1.0)

    # Draw the maze
    draw_maze()

    glutSwapBuffers()

def resize(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, float(width) / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def key_pressed(key, x, y):
    global player_angle
    if key == b'\x1b':  # ESC key
        sys.exit()
    elif key == b'a':
        player_angle += 0.1
    elif key == b'd':
        player_angle -= 0.1
    elif key in [b'w', b's', b'a', b'd']:
        keys[key] = True

def key_released(key, x, y):
    if key in [b'w', b's', b'a', b'd']:
        keys[key] = False

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D Maze")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glLightfv(GL_LIGHT0, GL_POSITION, (-1, -1, 1, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glutDisplayFunc(draw)
    glutReshapeFunc(resize)
    glutKeyboardFunc(key_pressed)
    glutKeyboardUpFunc(key_released)
    glutTimerFunc(0, update, 0)

    # Initialize keys dictionary
    keys[b'w'] = False
    keys[b's'] = False
    keys[b'a'] = False
    keys[b'd'] = False

    glutMainLoop()

if __name__ == "__main__":
    keys = {}
    main()
