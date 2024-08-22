from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-400, 250)
        self.write(f" level :{self.score}", align="left", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Courier", 25, "normal"))
    def increase_score(self):
        self.score += 1
