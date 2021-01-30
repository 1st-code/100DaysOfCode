from turtle import Turtle

FONT0 = ("Courier", 24, "normal")
FONT1 = ("Courier New", 12, "bold")
FONT2 = ("Courier New", 45, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1

        self.penup()
        self.color("#222")
        self.hideturtle()
        self.speed(-1)
        self.goto(-290, 280)

    def display(self):
        self.clear()
        self.goto(-290, 280)
        self.write(f"Level: {self.level}", align="left", font=FONT1)

    def game_over(self):
        self.goto(0, 0)
        self.color("#F00")
        self.write("GAME OVER", align="center", font=FONT2)

    def reset_score(self):
        self.clear()
        self.level = 0
        self.goto(-290, 280)
        self.color("#222")
        self.write(f"Level: {self.level}", align="left", font=FONT1)

