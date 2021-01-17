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
            self.BODY[-1].shape(snake_gfx[3])

    def move(self):
        """Sets Snake movement"""

        prev_x, prev_y = self.BODY[-1].pos()  # Tail position

        for i in range(len(self.BODY) - 1, 0, -1):  # BODY segments follow BODY[0]
            x, y = self.BODY[i - 1].pos()
            self.BODY[i].goto(x, y)
        else:
            new_x, new_y =  self.BODY[-1].pos()  # New Tail position

            # adjust tail gfx depending on direction of tail
            if new_x > prev_x:
                self.BODY[-1].shape(snake_gfx[3])
            elif new_y > prev_y:
                self.BODY[-1].shape(snake_gfx[2])
            elif new_y < prev_y:
                self.BODY[-1].shape(snake_gfx[1])
            elif new_x < prev_x:
                self.BODY[-1].shape(snake_gfx[4])

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

        if not (-310 < x < 310) or not (-340 < y < 300):
            return True
        else:
            return False
