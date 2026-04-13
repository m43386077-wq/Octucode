from time import sleep
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard

# Create the screen
screen = Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the ball
ball = Ball()
speed = 0.1

# Create the paddles
paddles = []
for i in range(2):
    paddle = Paddle(((-350, 350)[i], 0), ("red", "blue")[i])
    paddles.append(paddle)

# Create the scoreboard
scoreboard = ScoreBoard()

while True:

    screen.update()

    # Move the paddles
    screen.listen()
    screen.onkeypress(paddles[0].move_up, "w")
    screen.onkeypress(paddles[0].move_down, "s")
    screen.onkeypress(paddles[1].move_up, "Up")
    screen.onkeypress(paddles[1].move_down, "Down")

    # Move the ball
    ball.move()
    sleep(speed)

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles
    if (ball.distance(paddles[0]) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if(ball.distance(paddles[1]) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    # Detect if the ball goes out of bounds
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.left_point()
        speed *= 0.9

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.right_point()
        speed *= 0.9
