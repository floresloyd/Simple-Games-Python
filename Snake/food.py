from turtle import Turtle
import random


class Food(Turtle):  # INHERIT ALL ATTRIBUTES OF TURTLE CLASS
    # In snake class we don't inherit because we make our own snakes(turtle), using create_snake()
    def __init__(self):  # Here we manually only make one
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)