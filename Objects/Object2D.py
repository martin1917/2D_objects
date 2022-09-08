import math
from Matrix import Matrix

class Object2D:
    def __init__(self, vertexes: list[list[float]]):
        self.matrix = Matrix(
            [vec + [1] for vec in vertexes]
        )
    
    def move(self, dx, dy):
        self.matrix.mult(Matrix([
            [1, 0, 0],
            [0, 1, 0],
            [dx, dy, 1],
        ]))
    
    def scale(self, k):
        self.matrix.mult(Matrix([
            [k, 0, 0],
            [0, k, 0],
            [0, 0, 1]
        ]))
    
    def rotate(self, a):
        self.matrix.mult(Matrix([
            [math.cos(a), math.sin(a), 0],
            [-math.sin(a), math.cos(a), 0],
            [0, 0, 1],
        ]))