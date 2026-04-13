from time import sleep
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard

# Create the screen
screen = Screen()
screen.title("Paddle Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the ball
ball = Ball()
speed = 0.1

# Create the paddle
paddle = Paddle()

# Create the scoreboard
scoreboard = ScoreBoard()

while True:

    screen.update()

    # Move the paddles
    screen.listen()
    screen.onkeypress(paddle.move_right, "Right")
    screen.onkeypress(paddle.move_left, "Left")

    # Move the ball
    ball.fall()
    sleep(speed)

    if ball.ycor() < -290:
        ball.reset()
        speed *= 0.9
        continue

    if ball.distance(paddle) < 50 and ball.ycor() > -240:

        if ball.ball_shape == "triangle":
            scoreboard.reset()
            ball.reset()
            continue

        elif ball.ball_shape == "turtle" and ball.ball_color == "white":
            screen.bgcolor("red")
            scoreboard.game_over()
            break            

        scoreboard.point(ball.value)
        ball.reset()
        continue

screen.exitonclick()
