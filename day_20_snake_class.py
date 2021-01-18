import turtle
from turtle import Turtle
from day_20_snake_gfx import snake_gfx

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        for gfx in snake_gfx:
            turtle.register_shape(gfx)

        self.BODY = []
        self.new_snake()
        self.head = self.BODY[0]

    def new_snake(self):
        """Creates a list of SNAKE segments"""

        x, y = 0, 0

        for i in range(10):
            self.BODY.append(Turtle("square"))
            self.BODY[i].color("white")
            self.BODY[i].shape(snake_gfx[0])
            self.BODY[i].penup()
            self.BODY[i].setpos(x, y)
            x -= 20
        else:
            self.BODY[0].shape(snake_gfx[8])
            # self.BODY[-1].shape(snake_gfx[3])

    def move(self):
        """Sets Snake movement"""

        for i in range(len(self.BODY) - 1, 0, -1):  # BODY segments follow BODY[0]
            x, y = self.BODY[i - 1].pos()
            self.BODY[i].goto(x, y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.BODY[0].shape(snake_gfx[5])  # Tail Head Gfx Up

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.BODY[0].shape(snake_gfx[6])  # Tail Head Gfx Down

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.BODY[0].shape(snake_gfx[7])  # Tail Head Gfx Left

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.BODY[0].shape(snake_gfx[8])  # Tail Head Gfx Right

    def is_hit(self):
        """Checks if any segment of snake BODY is out of bounds"""

        x, y = self.head.position()

        if not (-305 < x < 305) or not (-305 < y < 305):
            return True
        else:
            return False
