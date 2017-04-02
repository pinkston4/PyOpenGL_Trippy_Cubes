import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cubes.green_cube import Green_cube
from cubes.red_cube import Red_cube
from cubes.blue_cube import Blue_cube
from cubes.little_black_cube import Black_cube


class Trippy(object):
    """
    The Trippy class is the main class of the application
    methods:
        __init__
        looper
    """
    def __init__(self, screen_width, screen_height):
        """
        Initializes application, sets the screen size, initializes cubes,
        sets the perspective, and calls the loop
        :param screen_width: width of screen
        :param screen_height: height of screen
        """
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.percpective = gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        self.step_back = glTranslatef(0.0, 0.0, -15)
        self.red_cube = Red_cube()
        self.green_cube = Green_cube()
        self.blue_cube = Blue_cube()
        self.black_cube = Black_cube()
        self.looper()

    def looper(self):
        """
        the while loop that makes the app run, listens for the quit event
        rotates and re-draws cubes
        :return:
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.blue_cube.draw_cube()
            self.green_cube.draw_cube()
            self.red_cube.draw_cube()
            self.black_cube.draw_cube()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == '__main__':
    width, height = 800, 600
    pygame.init()
    window = Trippy(width, height)
