from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_game()

    def update_game(self):
        self.clear()
        self.goto(-100, 350)
        self.write(self.l_score, align="center", font=("courier", 20, "normal"))
        self.goto(100, 350)
        self.write(self.r_score, align="center", font=("courier", 20, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_game()

    def increase_r_score(self):
        self.r_score += 1
        self.update_game()
