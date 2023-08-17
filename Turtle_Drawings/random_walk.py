import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.shape("arrow")
directions = [0, 90, 180, 270]
turtle.speed(10)
turtle.width(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


turtle_in_screen = True
while turtle_in_screen:
    turtle.color(random_color())
    turtle.forward(50)
    turtle.setheading(random.choice(directions))                # either this or random_move()


screen = t.Screen()
screen.exitonclick()