from turtle import Turtle
from time import sleep

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Ball(Turtle):

    def __init__(self, x, y):
        super().__init__()

        self.MOVE_X = 10
        self.MOVE_Y = 10

        self.startcoords = (x, y)
        self.MOVE_SPEED = 0.05
        self.penup()
        self.speed(-1)
        self.shape("circle")
        self.color("white")
        self.setpos(x, y)

    def move(self):
        """Sets ball movement"""

        self.bounce_y()

        sleep(self.MOVE_SPEED)
        new_x = self.xcor() + self.MOVE_X
        new_y = self.ycor() + self.MOVE_Y
        self.goto(new_x, new_y)

    def bounce_y(self):

        if self.ycor() >= 280:
            self.MOVE_Y = -10
        elif self.ycor() <= -280:
            self.MOVE_Y = 10

    def bounce_x(self, distance1, distance2):

        if (-330 > self.xcor() > -355) and distance1 <= 50:
            self.MOVE_X = 10
            self.MOVE_SPEED *= 0.93
        elif (330 < self.xcor() < 355) and distance2 <= 50:
            self.MOVE_X = -10
            self.MOVE_SPEED *= 0.93

    def not_in_play(self):
        if self.xcor() < -350 or self.xcor() > 350:
            return True
        else:
            return False

    def reset(self):

        self.setpos(self.startcoords)
        self.MOVE_SPEED = 0.05
