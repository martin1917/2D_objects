import tkinter as tk
from Objects.ComplexObject import ComplexObject
from common import DrawUtils
from Objects.Object2D import Object2D

class Object2DPrinter:
    def __init__(self, canvas):
        self.canvas = canvas #type: tk.Canvas

    def __draw_object(self, object):
        rows = object.matrix.rows
        for i in range(0, rows):
            curr_point = object.matrix.get_row(i)
            next_point = object.matrix.get_row((i+1) % rows)
            x1, y1 = DrawUtils.to_screen(curr_point)
            x2, y2 = DrawUtils.to_screen(next_point)
            self.canvas.create_line(x1, y1, x2, y2)
            self.canvas.create_oval(x1-2, y1-2, x1+2, y1+2, fill="red")
    
    def draw(self, object):
        if isinstance(object, ComplexObject):
            for part in object.parts:
                self.__draw_object(part)

        elif isinstance(object, Object2D):
            self.__draw_object(object)