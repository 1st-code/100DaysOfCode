from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()

        self.startcoords = (x, y)
        self.MOVE_SPEED = 20
        self.penup()
        self.speed(-1)
        self.shape("square")
        self.color("white")
        self.setheading(UP)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setpos(x, y)

    def up(self):
        """Move paddle up"""

        self.forward(self.MOVE_SPEED)
        self.MOVE_SPEED += 3

    def down(self):
        """Move paddle down"""

        self.backward(self.MOVE_SPEED)
        self.MOVE_SPEED += 3

    def key_depressed(self):

        self.MOVE_SPEED = 20

        return False

    def reset(self):

        self.setpos(self.startcoords)