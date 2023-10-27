from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)  # to disable automatic screen tracing / refresh / animation

left_paddle = Paddle(x_pos=-350, y_pos=0)
right_paddle = Paddle(x_pos=350, y_pos=0)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True

while is_game_on:
    ball.move_ball()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < 20 or \
            ball.xcor() < 320 and ball.distance(left_paddle) < 20:
        ball.bounce_x()

    # Check if ball goes out of bounds of window on left and right
    if ball.xcor() > 390:
        ball.start_again()
        scoreboard.l_point()
    elif ball.xcor() < -390:
        ball.start_again()
        scoreboard.r_point()

screen.exitonclick()
