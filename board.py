import colorsys
from tkinter import font
import turtle


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.screen = turtle.Screen()
        self.screen.setup(500, 500)
        self.screen.title("2048")
        self.pen = turtle.Turtle()
        self.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.hideturtle()
        self.draw_board()

    def draw_board(self):
        self.pen.clear()
        for i in range(self.size):
            for j in range(self.size):
                x = -self.size * 20 + j * 40
                y = self.size * 20 - i * 40
                self.pen.goto(x, y)
                self.pen.color("black", "white")
                self.pen.begin_fill()
                for _ in range(4):
                    self.pen.forward(40)
                    self.pen.right(90)
                self.pen.end_fill()


def draw_tile(x, y, value):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(colorsys[value])
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    if value > 0:
        turtle.color("black")
        turtle.up()
        turtle.goto(x + 50, y + 35)
        turtle.write(value, align="center", font=font)

    def update(self):
        for i in range(self.size):
            for j in range(self.size):
                self.draw_tile(i, j)
