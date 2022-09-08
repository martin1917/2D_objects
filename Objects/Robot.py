from Objects.ComplexObject import ComplexObject
from Objects.Object2D import Object2D

class Robot(ComplexObject):
    def __init__(self, x = 0, y = 0):
        self.head = Object2D([
            [60, 100],
            [60, 130],
            [90, 130],
            [90, 100],
        ])

        self.neck = Object2D([
            [70, 90],
            [70, 100],
            [80, 100],
            [80, 90],
        ])
        self.body = Object2D([
            [50, 30],
            [50, 90],
            [100, 90],
            [100, 30],
        ])
        self.left_ruka = Object2D([
            [40, 60],
            [40, 90],
            [50, 90],
            [50, 60],
        ])
        self.right_ruka = Object2D([
            [100, 80],
            [100, 90],
            [130, 90],
            [130, 80],
        ])
        self.left_neg = Object2D([
            [50, 0],
            [50, 30],
            [70, 30],
            [70, 0],
        ])
        self.right_neg = Object2D([
            [80, 0],
            [80, 30],
            [100, 30],
            [100, 0],
        ])

        self.parts = [
            self.head,
            self.neck,
            self.body,
            self.left_ruka,
            self.right_ruka,
            self.left_neg,
            self.right_neg,
        ]

        self.move(x, y)
        