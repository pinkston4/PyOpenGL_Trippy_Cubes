import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from .cube import Cube


class Red_cube(Cube):
    """

    """
    def __init__(self):
        Cube.__init__(self)
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )
        self.colors = (
            (0, 0, 0),
            (0.75, 0, 0),
            (0, 0, 0),
            (0.75, 0, 0),
            (0.75, 0, 0),
            (0.75, 0, 0),
            (0, 0, 0),
            (0.75, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0.75, 0, 0),
            (0.75, 0, 0),
        )
