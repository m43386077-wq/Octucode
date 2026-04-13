from time import sleep
from turtle import Screen
from snake import Snake
from food import Ball
from score import ScoreBoard

# Create a screen for the game
window = Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

snake = Snake()
food = Ball()
score = ScoreBoard()

while True:

    # move the snake
    snake.move()
    sleep(0.1)

    # control the snake with arrow keys
    window.listen()
    window.onkey(snake.up, "Up")
    window.onkey(snake.down, "Down")
    window.onkey(snake.left, "Left")
    window.onkey(snake.right, "Right")
    window.update()


    # Check for collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extand()
        score.increase_score()

    # Check for collision with wall
    head = snake.segments[0]
    if head.xcor() > 400 or head.xcor() < -400 or head.ycor() > 220 or head.ycor() < -300:
        score.save_high_score()
        window.bgcolor("red1")
        score.goto(0, 0)
        score.write("Game Over", align="center", font=("Courier", 48, "bold"))
        break

    
window.exitonclick()
