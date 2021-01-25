import time
import turtle
from turtle import Screen
from day_22_pong_paddle import Paddle
from day_22_pong_ball import Ball
from day_22_pong_scoreboard import Scoreboard


def main():
    global GAME_ON, FIRST_RUN

    screen.listen()

    while GAME_ON:

        ball.move()
        bounce()

        if FIRST_RUN:  # Load scoreboard do not reload unless score change
            scoreboard.display()
            FIRST_RUN = False

        if ball.not_in_play():
            if ball.xcor() > 450:
                score(1)
            elif ball.xcor() < -450:
                score(2)

        screen.update()

    screen.mainloop()


def paddle_reset():
    paddle_1.reset()
    paddle_2.reset()
    ball.reset()


def bounce():

    distance1 = paddle_1.distance(ball)
    distance2 = paddle_2.distance(ball)

    ball.bounce_x(distance1, distance2)


def score(player=False):

    if player == 1:
        scoreboard.player1_score += 1
        ball.MOVE_X = -10
    else:
        scoreboard.player2_score += 1
        ball.MOVE_X = 10

    scoreboard.display(player)
    scoreboard.player_win(player)
    time.sleep(2)
    scoreboard.display()
    ball.reset()


FIRST_RUN = True
GAME_ON = True
SPEED = 20

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("#222")  # Set background color
screen.title("Pong Game")

paddle_1 = Paddle(-356, 15)
paddle_2 = Paddle(350, 15)
ball = Ball(0, 15)
scoreboard = Scoreboard()

# screen.onkey(snake.up, "w")
# screen.onkey(snake.down, "s")
#

screen.onkeyrelease(paddle_2.key_depressed, "Up")
screen.onkeyrelease(paddle_2.key_depressed, "Down")
screen.onkeypress(paddle_2.up, "Up")
screen.onkeypress(paddle_2.down, "Down")
screen.onkeyrelease(paddle_1.key_depressed, "w")
screen.onkeyrelease(paddle_1.key_depressed, "s")
screen.onkeypress(paddle_1.up, "w")
screen.onkeypress(paddle_1.down, "s")

screen.onkeypress(paddle_reset, "Home")

screen.onkeypress(ball.move, "space")

main()
