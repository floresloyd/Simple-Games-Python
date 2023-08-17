import turtle as t
import random

### TURTLE ATTRIBUTES ###
turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
turtle.speed(0)
rgb_colors = [
            (213, 197, 255), (101, 190, 171), (100, 164, 209), (207, 137, 182),
            (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211),
            (25, 26, 26), (217, 163, 85)
]


def starting_position():
    turtle.penup()
    turtle.setx(-250)
    turtle.sety(-250)


def draw_dots():
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)


def turn_left():
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(50)


def turn_right():
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)


starting_position()
for _ in range(10):
    draw_dots()
    turn_left()
    draw_dots()
    turn_right()
screen = t.Screen()
screen.exitonclick()