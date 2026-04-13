from random import randint, choice
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.reset()
        self.value = 1

    def change_turtle(self):
        self.ball_shape = choice(["circle", "square", "triangle", "turtle"])
        self.ball_color = choice(["red", "green", "yellow", "purple", "orange", "white"])
        self.shape(self.ball_shape)
        self.color(self.ball_color)
        self.shapesize(randint(1, 3))
        self.value = 1 if self.ball_shape != "square" else 2

    def reset(self):
        self.change_turtle()
        self.hideturtle()
        self.goto(randint(-350, 350), 300)
        self.showturtle()

    def fall(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
