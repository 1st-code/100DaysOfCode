import turtle
from turtle import Turtle
from day_20_snake_gfx import snake_gfx

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle_cache = []  # List to cache old Turtle objects

class Snake:

    def __init__(self):

        for gfx in snake_gfx:
            turtle.register_shape(gfx)

        self.BODY = []
        self.new_snake()
        self.head = self.BODY[0]

    def new_snake(self):
        """Creates a list of SNAKE segments"""

        num, x, y = 3, 0, 0

        self.add_segment(num, x, y)
        self.BODY[0].shape(snake_gfx[8])

    def add_segment(self, num, x, y):
        for i in range(num):
            if len(turtle_cache) > 0:
                self.BODY.append(turtle_cache.pop())
            else:
                self.BODY.append(Turtle("square"))
            self.BODY[-1].color("white")
            self.BODY[-1].shape(snake_gfx[0])
            self.BODY[-1].penup()
            self.BODY[-1].setpos(x, y)

    def extend(self):
        """Adds a new segment to the Snake"""

        x, y = self.BODY[-1].pos()
        self.add_segment(1, x, y)

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
        """Checks for collision"""

        x, y = self.head.position()

        for _ in self.BODY[1:]:  # check for collision with body
            if _.distance(self.head) < 10:
                return True

        if not (-305 < x < 305) or not (-305 < y < 305):  # check if out of bounds
            return True
        else:
            return False

    def reset_game(self):

        for _ in self.BODY[3:]:
            _.goto(0, 800)

        while len(self.BODY) > 3:
            turtle_cache.append(self.BODY.pop())  # Caches old Turtle objects in list

        for _ in self.BODY:
            _.goto(0, 0)
            _.setheading(0)
            self.right()
