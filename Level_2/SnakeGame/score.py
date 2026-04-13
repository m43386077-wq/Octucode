from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(-390, 230)
        self.pendown()
        self.forward(780)
        self.penup()
        self.goto(0, 240)
        self.write(f"Score: {self.score}        High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()
