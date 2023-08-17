import turtle as t
import random

turtle = t.Turtle()
turtle.width(5)
t.colormode(255)
turtle.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_shape(number_of_sides):
    turtle.pendown()
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        turtle.right(angle)
        turtle.forward(100)


for i in range(3, 11):
    turtle.color(random_color())
    draw_shape(i)


screen = t.Screen()
screen.exitonclick()