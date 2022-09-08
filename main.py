import math
import tkinter as tk
from Objects.Robot import Robot
from common import DrawUtils
from common.Consts import Consts
from Objects.House import House
from Object2DPrinter import Object2DPrinter
from Objects.Object2D import Object2D

# отрисовка осей XOY
def draw_axies(canvas: tk.Canvas) -> None:
    x0, y0 = DrawUtils.to_screen([0, 0])
    x1, y1 = DrawUtils.to_screen([Consts.WIDTH - Consts.X0, 0])
    x2, y2 = DrawUtils.to_screen([0, Consts.HEIGHT - Consts.Y0])
    canvas.create_line(x0, y0, x1, y1, arrow=tk.LAST)
    canvas.create_line(x0, y0, x2, y2, arrow=tk.LAST)
    canvas.create_oval(x0-3, y0-3, x0+3, y0+3, fill="blue")

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=Consts.WIDTH, height=Consts.HEIGHT, bg="white")
    canvas.pack()
    printer = Object2DPrinter(canvas)

    # рисуем оси
    draw_axies(canvas)

    # создание робота
    robot = Robot()

    # рисуем робота в начале
    printer.draw(robot)

    # меняем парамаетры робота
    robot.scale(2)
    robot.move(100, 100)
    robot.rotate(math.radians(20))

    # рисуем робота после изменений
    printer.draw(robot)

    # создание дома
    house = House()

    # меняем парамаетры дома
    house.scale(3)
    house.move(250, 200)
    house.rotate(math.radians(-25))

    # рисуем дом после изменений
    printer.draw(house)

    root.mainloop()
    
if __name__ == "__main__":
    main()