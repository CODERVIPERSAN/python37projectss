from turtle import Turtle


class Score(Turtle):
    def __init__(self, lefti):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.pencolor("white")
        self.left(90)
        self.forward(280)
        self.left(lefti)
        self.forward(300)
        self.write(arg=f"score{self.score}", font=("Arial", 50,"normal"))

    def score_increment(self):
        self.score+=1
        self.write(arg=f"score{self.score}",font=("Arial",50,"normal"))

    def game_over(self,winner):
        self.setpos(-300,0)
        self.write(arg =f"game over {winner} wins the game ")