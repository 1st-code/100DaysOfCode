import turtle
from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.BODY = []
        self.new_snake()
        self.head = self.BODY[0]

    def new_snake(self):
        """Creates a list of SNAKE segments"""

        x, y = 0, 0

        for i in range(6):
            self.BODY.append(Turtle("square"))
            self.BODY[i].color("white")
            self.BODY[i].penup()
            self.BODY[i].setpos(x, y)
            x -= 20

    def move(self):
        """Sets Snake movement"""

        for i in range(len(self.BODY) - 1, 0, -1):  # BODY segments follow BODY[0]
            x, y = self.BODY[i - 1].pos()
            self.BODY[i].goto(x, y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def is_hit(self):
        """Checks if any segment of snake BODY is out of bounds"""

        x, y = self.head.position()

        if not (-300 < x < 300) or not (-300 < y < 300):
            return True
        else:
            return False
