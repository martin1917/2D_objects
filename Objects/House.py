from Objects.ComplexObject import ComplexObject
from Objects.Object2D import Object2D


class House(ComplexObject):
    def __init__(self, x = 0, y = 0):
        self.center = Object2D([
            [20, 0],
            [20, 35],
            [40, 35],
            [40, 0],
        ])
        self.krisha = Object2D([
            [20, 35],
            [30, 45],
            [40, 35],
        ])
        self.door = Object2D([
            [30, 0],
            [30, 15],
            [35, 15],
            [35, 0],
        ])

        self.parts = [
            self.center,
            self.krisha,
            self.door,
        ]

        self.move(x, y)