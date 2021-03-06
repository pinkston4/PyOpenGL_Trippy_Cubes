from .cube import Cube

class Green_cube(Cube):
    """
    the green cube size and color
    """
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
            (0, 1, 0),
            (0, 0, 0),
            (0, 1, 0),
            (0, 1, 0),
            (0, 1, 0),
            (0, 0, 0),
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 1, 0),
            (0, 1, 0),
        )

