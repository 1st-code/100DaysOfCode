import turtle
from turtle import Turtle, register_shape
from random import randint

CHERRY_GFX = 'gfx/cherry.gif'


class Food(Turtle):

    def __init__(self):
        super().__init__()
        turtle.register_shape(CHERRY_GFX)
        self.shape(CHERRY_GFX)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(-1)
        self.refresh()

    def refresh(self):

        random_x = randint(-280, 280)
        random_y = randint(-280, 280)

        while random_x % 20 != 0:
            random_x = randint(-280, 280)
        while random_y % 20 != 0:
            random_y = randint(-280, 280)

        self.goto(random_x, random_y)
