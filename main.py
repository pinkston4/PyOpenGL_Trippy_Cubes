import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubes.green_cube import Green_cube


class Trippy(object):
    """

    """
    def __init__(self, screen_width, screen_height):
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.green_cube = Green_cube()
        self.looper()

    def looper(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glRotatef(self.green_cube.rotation[0], self.green_cube.rotation[1],
                      self.green_cube.rotation[2], self.green_cube.rotation[3])
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.green_cube.draw_cube()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == '__main__':
    width, height = 800, 600
    pygame.init()
    window = Trippy(width, height)
