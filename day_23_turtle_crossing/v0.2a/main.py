from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():

    screen.listen()

    if FIRST_RUN:
        cars.add_car(20)

    game_loop()

    screen.mainloop()


def game_loop():
    """game loop, start car movement, check car placement, if player has event"""

    global GAME_ON, FIRST_RUN

    if not GAME_ON:  # if not GAME_ON, exit game_loop
        return

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
        screen_flash()
        player.hit()
        scoreboard.game_over()
        screen.ontimer(reset_game, 5000)
        return

    # Level Up
    x, y = player.current_position()
    if y > 260:
        scoreboard.level += 1
        scoreboard.display()
        GAME_ON = False
        player.turnaround()
        screen.ontimer(level_up, 2500)
        return

    screen.update()  # update screen

    screen.ontimer(game_loop, 5)  # repeat game_loop() after set period


def level_up():
    global GAME_ON, COUNT

    COUNT = 2

    cars.MOVE_INCREMENT += 1
    cars.add_car(2)
    player.default_frame()
    screen_flash()
    player.reset_position()
    GAME_ON = True

    main()


def screen_flash():
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
    screen.ontimer(screen_flash, 150)


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

