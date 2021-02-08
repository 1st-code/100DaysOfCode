import turtle
from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

LEFT = 180
RIGHT = 0

PLAYER_GFX = [
          ["gfx/bear_fall_0.gif", "gfx/bear_fall_1.gif", "gfx/bear_fall_2.gif"],
          ["gfx/bear_jump_0.gif", "gfx/bear_jump_1.gif", "gfx/bear_jump_2.gif", "gfx/bear_jump_3.gif"],
          ["gfx/bear_turn_0.gif", "gfx/bear_turn_1.gif", "gfx/bear_turn_2.gif", "gfx/bear_turn_3.gif"],
]


class Player(Turtle):

    def __init__(self):
        super().__init__()

        for item in PLAYER_GFX:
            for i in range(len(item)):
                turtle.register_shape(item[i])

        # animation counts
        self.frame_a = 0
        self.frame_b = 0
        self.frame_c = 0

        self.penup()
        self.shape(PLAYER_GFX[1][0])
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """Move forward + animation"""

        self.forward(3)

        if self.frame_a <= 3:
            self.shape(PLAYER_GFX[1][self.frame_a])
            self.frame_a += 1
        else:
            self.shape(PLAYER_GFX[1][0])
            self.frame_a = 0
            return

        Screen().ontimer(self.move, 150)

    def turnaround(self):
        """Bear turns around animation"""

        if self.frame_b <= 3:
            self.shape(PLAYER_GFX[2][self.frame_b])
            Screen().update()
            self.frame_b += 1
        else:
            self.frame_b = 0
            return

        Screen().ontimer(self.turnaround, 250)

    def hit(self):
        """Bear hit animation"""

        if self.frame_c <= 2:
            self.shape(PLAYER_GFX[0][self.frame_c])
            Screen().update()
            self.frame_c += 1
        else:
            self.frame_c = 0
            return

        Screen().ontimer(self.hit, 250)

    def default_frame(self):
        self.shape(PLAYER_GFX[1][0])

    def move_to_mouse(self, x, y):
        self.ondrag(None)
        self.goto(x, y)

    def current_position(self):
        x, y = self.position()
        x, y = int(x), int(y)
        return x, y

    def reset_position(self):

        self.goto(STARTING_POSITION)
