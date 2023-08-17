from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]                      # Starting position for the first 3 segments
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # WE DON'T INHERIT FROM TURTLE SINCE WE JUST USE IT TO CREATE TURTLES/SNAKE SEGMENTS
    def __init__(self):                                               # DEFAULT CONSTRUCTOR
        self.snake_segments = []                                      # Segments are placed in a list
        self.create_snake()                                           # Creates the first 3 snake segments
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:                           # First 3 segments that you start with are created
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())       # Take position of last so we can add another one

    def move(self):
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):  # Loop through from last segment to the first
            ### SNAKE MOVEMENT - Last overtakes Second, Second Overtakes First, Then first takes the charge again
            new_x = self.snake_segments[segment_index - 1].xcor()                # Get a hold of the second to the last index --
            new_y = self.snake_segments[segment_index - 1].ycor()                # -- so we can get its position
            self.snake_segments[segment_index].goto(new_x, new_y)                # and make the last index take its spot
        self.snake_segments[0].forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
