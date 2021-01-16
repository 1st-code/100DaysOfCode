import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)

screen.register_shape("gfx/pencil.gif")
screen.register_shape("gfx/pencil_r.gif")
screen.register_shape("gfx/pencil_g.gif")
screen.register_shape("gfx/pencil_b.gif")
screen.register_shape("gfx/pencil_w.gif")

t = Turtle("turtle")
t.speed(-1)

t.shape("gfx/pencil.gif")

def brush_white():
    t.shape("gfx/pencil_w.gif")
    t.color("white")

def brush_black():
    t.shape("gfx/pencil.gif")
    t.color("black")

def brush_red():
    t.shape("gfx/pencil_r.gif")
    t.color("red")

def brush_green():
    t.shape("gfx/pencil_g.gif")
    t.color("lime")

def brush_blue():
    t.shape("gfx/pencil_b.gif")
    t.color("blue")

def increase_brush():
    size = int(t.pensize())
    size += 2
    t.pensize(size)

def decrease_brush():
    size = int(t.pensize())

    if size >= 3:
        size -= 2
        t.pensize(size)

def draw(x, y):
    t.ondrag(None)
    t.pendown()
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(draw)

def undo(x, y):
    t.undo()

def clear_screen(x, y):
    t.clear()

def move_to_mouse(x, y):
    t.ondrag(None)
    t.penup()
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(draw)

def main():
    turtle.listen()

    t.ondrag(draw)

    screen.onclick(move_to_mouse, 1)
    screen.onclick(undo, 2)
    screen.onclick(clear_screen, 3)

    turtle.onkeypress(increase_brush, "=")
    turtle.onkeypress(increase_brush, "+")
    turtle.onkeypress(decrease_brush, "-")

    turtle.onkeypress(brush_red, "r")
    turtle.onkeypress(brush_green, "g")
    turtle.onkeypress(brush_blue, "b")
    turtle.onkeypress(brush_white, "w")
    turtle.onkeypress(brush_black, "p")

    screen.mainloop()


main()