from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1.2,stretch_len=1.2)
        self.color("white")
        self.penup()
        self.x_move = 20
        self.y_move = 20
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move


        self.setpos(new_x,new_y)

    def bounce(self):
        if self.ycor()>=300 or self.ycor()<=-300:
                  #to bounce
            self.y_move *= -1
    def reset_position(self):
        self.setpos(0,0)
        self.x_move *= -1
