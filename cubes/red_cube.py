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
            (1, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (1, 0, 0),
        )
        self.surfaces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )
        self.rotation = (1, 3, 1, 1)
