from turtle import Turtle

FONT = ("Courier New", 18, "bold")
FONT2 = ("Courier New", 28, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("#1E6C00")
        self.hideturtle()
        self.speed(-1)
        self.goto(0, 270)

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT2)