from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self,stretch_len,stretch_wid,color,):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=stretch_len, stretch_wid=stretch_wid)
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_randomx = randint(-300 ,300)
        new_randomy = randint(-300 ,300)
        self.goto(new_randomx ,new_randomy)