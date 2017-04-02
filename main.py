import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubes.green_cube import Green_cube
from cubes.red_cube import Red_cube


class Trippy(object):
    """

    """
    def __init__(self, screen_width, screen_height):
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.percpective = gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        self.step_back = glTranslatef(0.0, 0.0, -15)
        self.red_cube = Red_cube()
        self.green_cube = Green_cube()
        self.cubes = (self.red_cube, self.green_cube)
        self.looper()

    def looper(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.green_cube.rotate_cube()
            self.red_cube.rotate_cube()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.green_cube.draw_cube()
            self.red_cube.draw_cube()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == '__main__':
    width, height = 800, 600
    pygame.init()
    window = Trippy(width, height)
