from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.hideturtle()
        self.left(90)
        self.forward(300)
        self.pensize(100)
        self.color("white")
        with open("C:\\Users\\Santhosh R\\PycharmProjects\\100daysofcode_angela_yu\\24thday working with local file "
                  "system  and directory\\high_score.txt") as high:
            self.high_score = int(high.read())

        self.write(arg=f"Score{self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def score_increment(self, step):
        self.score += step

        self.write(arg=f"Score{self.score}---high_score{self.high_score}", move=False, align="center", font=("Arial", 30, "normal"))

    # def gameover(self):
    #     self.setpos(-300,0)
    #     self.write(arg="Game over",font=("Arial",75,"normal"))
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            with open("C:\\Users\\Santhosh R\\PycharmProjects\\100daysofcode_angela_yu\\24thday working with local "
                      "file system  and directory\\high_score.txt", "w") as high:
                high.write(str(self.score))
            with open("C:\\Users\\Santhosh R\\PycharmProjects\\100daysofcode_angela_yu\\24thday working with local "
                      "file system  and directory\\high_score.txt") as high:
                self.high_score = int(high.read())
        self.score = 0
        self.write(f"Score{self.score}  highscore{self.high_score}", align="center", font=("Arial", 30, "normal"))
