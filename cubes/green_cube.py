import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .cube import Cube

class Green_cube(Cube):

    def __init__(self):
        Cube.__init__(self)
        self.vertices = (
            (2, -2, -2),
            (2, 2, -2),
            (-2, 2, -2),
            (-2, -2, -2),
            (2, -2, 2),
            (2, 2, 2),
            (-2, -2, 2),
            (-2, 2, 2)
        )
        self.colors = (
            (0, 0, 0),
            (0, 0.5, 0),
            (0, 0, 0),
            (0, 0.5, 0),
            (0, 0.5, 0),
            (0, 0.5, 0),
            (0, 0, 0),
            (0, 0.5, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0.5, 0),
            (0, 0.5, 0),
        )

