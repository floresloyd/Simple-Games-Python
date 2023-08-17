from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 8, 'normal')
GAME_OVER_FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    # We just inherit from turtle class and don't need to create a turtle object
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score_counter = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score_counter}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score_counter += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAME OVER! \n    Score: {self.score_counter}",
            move=False,
            align=ALIGNMENT, font=GAME_OVER_FONT)