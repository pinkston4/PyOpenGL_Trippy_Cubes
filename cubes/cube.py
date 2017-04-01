import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Cube:
    """

    """
    def __init__(self):
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
        self.edges = (
            (0, 1),
            (0, 3),
            (0, 4),
            (2, 1),
            (2, 3),
            (2, 7),
            (6, 3),
            (6, 4),
            (6, 7),
            (5, 1),
            (5, 4),
            (5, 7)
        )

    def draw_cube(self):
        """
        glBegin(GL_QUADS) then iterate over each surface and
        for each vertex in that surface tuple color the space

        glBegin(GL_LINES) iterates over the edges and vertices in those
        edges and maps the edges and lines based on those vertices
        """
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            x = 0
            for vertex in surface:
                glColor3fv(self.colors[x])
                glVertex3fv(self.vertices[vertex])
                x += 1

        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

