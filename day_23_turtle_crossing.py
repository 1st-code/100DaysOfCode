from turtle import Screen
from day_23_turtle_crossing_player import Player
from day_23_turtle_crossing_car_manager import CarManager
from day_23_turtle_crossing_scoreboard import Scoreboard


def main():
    global GAME_ON, FIRST_RUN

    screen.listen()

    if len(cars.cars) < 25:
        cars.add_car(20)

    while GAME_ON:

        if FIRST_RUN:  # Load scoreboard
            scoreboard.display()
            cars.move()
            FIRST_RUN = False

        cars.reset_cars()
        cars.check_overlap()

        # Hit car
        if cars.is_hit(player.current_position()):
            GAME_ON = False
            cars.game_over()
            game_over()
            player.hit()
            scoreboard.game_over()
            screen.ontimer(reset_game, 5000)

        # Level Up
        x, y = player.current_position()
        if y > 260:
            scoreboard.level += 1
            scoreboard.display()
            GAME_ON = False
            player.turnaround()
            screen.ontimer(level_up, 2500)

        screen.update()

    screen.mainloop()


def level_up():
    global GAME_ON

    cars.MOVE_INCREMENT += 1
    cars.add_car(2)
    player.default_frame()
    player.reset_position()
    GAME_ON = True

    main()


def game_over():
    global COUNT

    if COUNT >= 4:
        COUNT = 0
        return
    elif screen.bgpic() == "gfx/bg.png":
        screen.bgcolor("#FFF")
        screen.bgpic("gfx/bg_invert.png")
    elif screen.bgpic() == "gfx/bg_invert.png":
        screen.bgcolor("#888")
        screen.bgpic("gfx/bg.png")

    COUNT += 1
    screen.ontimer(game_over, 150)


def reset_game():
    global GAME_ON

    cars.reset_game()
    player.default_frame()
    player.reset_position()
    scoreboard.reset_score()
    GAME_ON = True

    main()


FIRST_RUN = True
GAME_ON = True
COUNT = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("#888")  # Set background color
screen.bgpic("gfx/bg.png")
screen.title("Bear Crossing")

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkey(player.move, "Up")

main()

