from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-380, 380)
        y_pos = random.randint(-270, 270)
        self.goto(x_pos, y_pos)
