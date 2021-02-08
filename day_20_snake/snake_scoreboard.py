from turtle import Turtle

FONT = ("Courier New", 18, "bold")
FONT2 = ("Courier New", 28, "bold")

score_file_read = open("highscore", "r")
try:
    temp_score = int(score_file_read.read())  # read high score from save file
except ValueError:
    temp_score = 0
score_file_read.close()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = temp_score
        self.score = 0
        self.penup()
        # self.color("#1E6C00")
        self.color("#FFF")
        self.hideturtle()
        self.speed(-1)
        self.goto(0, 270)

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}  (High Score: {self.highscore})", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("#FFF")
        self.write("GAME OVER", align="center", font=FONT2)

    def reset_score(self):
        self.clear()
        self.score = 0
        self.goto(0, 270)

    def save_score(self):
        if self.score > self.highscore:
            score_file = open("highscore", "w")
            self.highscore = self.score
            score_file.write(str(self.highscore))
            score_file.close()
