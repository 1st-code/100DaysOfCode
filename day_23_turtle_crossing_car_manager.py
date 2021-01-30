import turtle
from turtle import Turtle, Screen
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# List of starting coordinates for cars
Y_COORDS = [-224, -194, -164, -134, -104, -74, -44, -14, 16, 46, 76, 106, 136, 166, 196, 230]
X_COORDS = [320, 350, 390, 420, 450]

X_OFFSET = [70, 120, 160, 250, 400]
STARTING_MOVE_DISTANCE = 5

STATUS = True
LEFT = 180
RIGHT = 0

CAR_GFX = [
          ["gfx/car_0_0.gif", "gfx/car_0_1.gif", "gfx/car_0_2.gif", "gfx/car_0_3.gif"],
          ["gfx/car_1_0.gif", "gfx/car_1_1.gif", "gfx/car_1_2.gif", "gfx/car_1_3.gif"],
          ["gfx/car_2_0.gif", "gfx/car_2_1.gif", "gfx/car_2_2.gif", "gfx/car_2_3.gif"],
          ["gfx/car_3_0.gif", "gfx/car_3_1.gif", "gfx/car_3_2.gif", "gfx/car_3_3.gif"],
          ["gfx/car_4_0.gif", "gfx/car_4_1.gif", "gfx/car_4_2.gif", "gfx/car_4_3.gif"],
          ["gfx/car_5_0.gif", "gfx/car_5_1.gif", "gfx/car_5_2.gif", "gfx/car_5_3.gif"],
          ["gfx/car_6_0.gif", "gfx/car_6_1.gif", "gfx/car_6_2.gif", "gfx/car_6_3.gif"],
          ["gfx/car_7_0.gif", "gfx/car_7_1.gif", "gfx/car_7_2.gif", "gfx/car_7_3.gif"],
          ["gfx/car_8_0.gif", "gfx/car_8_1.gif", "gfx/car_8_2.gif", "gfx/car_8_3.gif"],
          ["gfx/car_9_0.gif", "gfx/car_9_1.gif", "gfx/car_9_2.gif", "gfx/car_9_3.gif"],
          ["gfx/car_10_0.gif", "gfx/car_10_1.gif", "gfx/car_10_2.gif", "gfx/car_10_3.gif"]
]

CAR_COLORS = []

CARS_CACHE = []  # List to cache old Turtle objects


class CarManager():

    def __init__(self):
        super().__init__()

        self.cars = []
        self.MOVE_INCREMENT = 4

        for item in CAR_GFX:
            for i in range(4):
                turtle.register_shape(item[i])

        self.add_car()

    def add_car(self, num=1):
        """Adds parameter (num) amount of cars"""

        for i in range(num):
            new_car = Turtle()
            new_car.penup()
            gfx_car = choice(CAR_GFX)
            new_car.shape(gfx_car[0])
            new_car.setheading(180)
            new_car.goto(choice(X_COORDS), choice(Y_COORDS))
            for car in self.cars:
                if new_car.distance(car["car"]) < 50:
                    new_car.goto(new_car.xcor() + choice(X_OFFSET), new_car.ycor())
            dict_car = {"car": new_car, "car_color": gfx_car}

            self.cars.append(dict_car)

    def move(self):
        """Move forward + animation"""

        for car in self.cars:

            car["car"].forward(self.MOVE_INCREMENT)

            if car["car"].shape() == car["car_color"][0]:
                car["car"].shape(car["car_color"][1])
            elif car["car"].shape() == car["car_color"][1]:
                car["car"].shape(car["car_color"][2])
            elif car["car"].shape() == car["car_color"][2]:
                car["car"].shape(car["car_color"][3])
            elif car["car"].shape() == car["car_color"][3]:
                car["car"].shape(car["car_color"][0])

        Screen().ontimer(self.move, 150)

    def reset_cars(self):
        """Checks for cars moved off screen"""

        for car in self.cars:
            if car["car"].xcor() < -330:
                car["car"].hideturtle()
                self.cars.remove(car)
                self.add_car()

    def check_overlap(self):
        """checks for cars overlapping same screen space"""

        for car in self.cars:
            for other_car in self.cars:
                if car["car"].xcor() != other_car["car"].xcor():
                    if car["car"].distance(other_car["car"]) < 40:
                        car["car"].goto(car["car"].xcor() + 40, car["car"].ycor())

    def is_hit(self, player_position):
        """Checks for player collision with cars"""

        for car in self.cars:
            car_x, car_y = car["car"].position()
            player_x, player_y = player_position
            if car["car"].distance(player_position) < 40 and (car_y - 10) < player_y < (car_y + 10) \
                    and player_x <= (car_x + 6):
                return True

    def reset_game(self):

        for car in self.cars:
            car["car"].hideturtle()

        while len(self.cars) > 0:
            self.cars.pop()

        self.add_car(13)
        self.MOVE_INCREMENT = 4

    def move_to_mouse(self, x, y):
        self.cars[0]["car"].ondrag(None)
        self.cars[0]["car"].goto(x, y)

    def game_over(self):

        self.MOVE_INCREMENT = 0

