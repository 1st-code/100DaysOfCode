import time
import turtle
from turtle import Screen
from day_20_snake_class import Snake
from day_20_snake_food import Food
from day_20_snake_scoreboard import Scoreboard


def main():
    global GAME_ON, FIRST_RUN, SCORE

    if FIRST_RUN:
        time.sleep(4)
        screen.bgpic("gfx/snake_bg_transp.gif")
        FIRST_RUN = False

    screen.listen()

    while GAME_ON:

        scoreboard.display()
        turtle.update()
        time.sleep(.12)

        snake.move()

        if snake.is_hit():
            # GAME_ON = False
            scoreboard.game_over()
            time.sleep(4)
            snake.reset_game()
            scoreboard.reset_score()
            food.refresh()
            continue

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.score += 1
            scoreboard.save_score()
            snake.extend()

    screen.mainloop()


FIRST_RUN = True
GAME_ON = True

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("#222")  # Set background color
screen.bgpic("gfx/snake_bg_pixelart_transp.gif")  # Sets pixelart logo
turtle.update()  # required to display pixelart because of screen.tracer()
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

main()
