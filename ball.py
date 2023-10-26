from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()

    def move_ball(self):
        time.sleep(0.1)
        self.goto(self.xcor() + 10, self.ycor() + 10)
