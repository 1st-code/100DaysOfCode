import time
import turtle
from turtle import Screen
from day_20_snake_class import Snake


def main():
    global GAME_ON

    screen.listen()

    while GAME_ON:

        turtle.update()
        time.sleep(.15)

        snake.move()

        if snake.is_hit():
            GAME_ON = False
            continue

    screen.mainloop()


GAME_ON = True

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("#555")
screen.bgpic("gfx/snake_bg.gif")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

main()
