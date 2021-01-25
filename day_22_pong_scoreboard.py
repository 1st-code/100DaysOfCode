from turtle import Turtle

FONT = ("Courier New", 60, "bold")
FONT2 = ("Consolas", 32, "bold")
FONT3 = ("Wide Latin", 72, "bold")

score_file_read = open("day_22_pong_highscore", "r")
try:
    temp_score = score_file_read.read()  # read high score from save file
    temp_score = temp_score.split(',')
    for item in temp_score:
        item = int(item)
        print(type(item), item)
except ValueError:
    temp_score = [0, 0]
score_file_read.close()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = temp_score
        self.player1_score = 0
        self.player2_score = 0
        self.penup()
        self.color("#FFF")
        self.hideturtle()
        self.speed(-1)

    def display(self, new_score=False):
        self.clear()
        self.goto(0, -40)
        self.color("#333")
        self.write(f"PONG", align="center", font=FONT3)
        self.color("#FFF")
        if new_score == 1:
            self.color("#0F0")
        self.goto(-100, 200)
        self.write(f"{self.player1_score}", align="left", font=FONT)
        self.color("#FFF")
        if new_score == 2:
            self.color("#0F0")
        self.goto(100, 200)
        self.write(f"{self.player2_score}", align="right", font=FONT)
        self.color("#FFF")

    def player_win(self, winner):
        self.goto(0, 140)
        self.color("#0F0")
        self.write(f"PLAYER {winner}", align="center", font=FONT2)

    def reset_score(self):
        self.clear()
        self.player1_score = 0
        self.player2_score = 0
        self.display()

    def save_score(self):
        if (self.player1_score > self.highscore[0]) or (self.player2_score > self.highscore[1]):
            score_file = open("day_22_pong_highscore", "w")
            score_file.write(f"{self.player1_score},{self.player2_score}")
            score_file.close()
