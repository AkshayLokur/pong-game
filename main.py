from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)  # to disable automatic screen tracing / refresh / animation

left_paddle = Paddle(x_pos=350, y_pos=0)
right_paddle = Paddle(x_pos=-350, y_pos=0)

screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")

ball = Ball()

is_game_on = True

while is_game_on:
    ball.move_ball()
    screen.update()

screen.exitonclick()
