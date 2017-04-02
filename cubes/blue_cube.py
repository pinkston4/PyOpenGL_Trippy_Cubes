import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .cube import Cube

class Blue_cube(Cube):

    def __init__(self):
        Cube.__init__(self)
        self.vertices = (
            (3, -3, -3),
            (3, 3, -3),
            (-3, 3, -3),
            (-3, -3, -3),
            (3, -3, 3),
            (3, 3, 3),
            (-3, -3, 3),
            (-3, 3, 3)
        )
        self.colors = (
            (0, 0, 0),
            (0, 0, .5),
            (0, 0, 0),
            (0, 0, 0.5),
            (0, 0, 0.5),
            (0, 0, 0.5),
            (0, 0, 0),
            (0, 0, 0.5),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0.5),
            (0, 0, 0.5),
        )

