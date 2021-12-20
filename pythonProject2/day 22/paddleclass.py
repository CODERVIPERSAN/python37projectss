
from turtle import Turtle, Screen, colormode
colormode(255)


class Paddle(Turtle):
    def __init__(self, position_of_paddle, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.setpos(position_of_paddle)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)


    def move_front(self):
        xcor = self.pos()[0]
        ycor = self.pos()[1]
        print(ycor)
        new_pos = ycor + 20
        self.setpos(xcor,new_pos)

    def move_back(self):
        ycor = self.pos()[1]
        xcor = self.pos()[0]
        new_pos = ycor - 20

        self.setpos(xcor, new_pos)
