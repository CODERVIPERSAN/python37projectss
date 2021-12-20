from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.penup()
        self.color("black")
        self.setpos(-280, 280)
        self.write(arg=f"score: {self.score} ", font=FONT, move=False)

    def increment_score(self):
        self.score += 1
        self.setpos(-280,280)
        self.write(arg=f"score:{self.score}", font=FONT, move=False)

    def game_over(self):
        self.write(arg="Game over ",font= FONT,move=False)