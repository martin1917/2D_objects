from Objects.Object2D import Object2D


class ComplexObject(Object2D):
    def __init__(self):
        self.parts = None # type: list[Object2D]
    
    def move(self, dx, dy):
        for part in self.parts:
            part.move(dx, dy)
    
    def scale(self, k):  
        for part in self.parts:
            part.scale(k)
    
    def rotate(self, a):
        for part in self.parts:
            part.rotate(a)