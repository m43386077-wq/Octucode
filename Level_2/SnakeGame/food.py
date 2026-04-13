import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.turtlesize(0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-380, 380)
        y = random.randint(-280, 200)
        self.goto(x, y)
        