import Matrix
from common.Exceptions import *

class Matrix:
    def __init__(self, map: list[list[float]]):
        if(len(map) == 0 or len(map[0]) == 0):
            raise MatrixCreateException()

        self.map = map
        self.rows = len(map)
        self.cols = len(map[0])
    
    def mult(self, other: Matrix):
        if self.cols != other.rows:
            raise MultOfMatrixException()

        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    result[i][j] += self.map[i][k] * other.map[k][j]
        
        self.map = result
    
    def get_row(self, i):
        if(0 <= i <= self.rows):
            return self.map[i]