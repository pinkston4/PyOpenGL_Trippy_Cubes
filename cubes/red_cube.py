from .cube import Cube


class Red_cube(Cube):
    """
    the red cube size and color
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
