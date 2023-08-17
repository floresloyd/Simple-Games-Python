from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.goto(-240, 240)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!",
            move=False,
            align="center",
            font=FONT
                   )



