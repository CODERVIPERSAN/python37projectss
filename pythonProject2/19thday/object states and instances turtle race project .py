import turtle
from turtle import Turtle, Screen
import random
import time

# object states and instances

# many object can be created by the one blue print class

# each object function  independent ----  in programing
# we say separate instances

# turtle1.color="green"   their state
# turtle2.color = "purple"  their states   differences states

# states is nothing the turtle object varies with other object in
# appearance or in doing methods and behaviour
# turtle coordinate system
screen = Screen()
screen.setup(height=700, width=900)

user_guess = screen.textinput(title="TuRtLe TuRt", prompt="guess which turtle will make make the end  line ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange"]
screen.tracer(0)

turtle.penup()
turtle.setpos(400, 300)
turtle.pendown()
turtle.setpos(400, -300)
for i in range(-3, 3):
    tim1 = Turtle(shape="turtle")
    tim1.color(colors[i + 2])
    tim1.penup()
    tim1.setpos(-400, i * 100)

    # print(tim1.pos())
    # endgame = False
    # while not(endgame) :
    #     tim1.forward(random.randint(1,50))
    #     if tim1.pos()[0]==300:
    #         endgame = True
    #         print("colour is the winner ")

endgame = False
while not endgame:
    for turt in turtle.turtles()[1:]:
        turt.forward(random.randint(1, 25))
        pos = turt.pos()
        if pos[0] > 400:
            if turt.pencolor() == user_guess:
                print("u bet it right ")
            else:
                print("wrong bet ")
            print(f"{turt.pencolor()} is the winner ")
            endgame = True
            break
    time.sleep(0.1)
    screen.update()
# import random
# class intialsetup:
#     def __init__(self, x, y, color):
#         """make a initial setup for the gap and specify the position
#         to start the race  x,y as parameter"""
#         self =Turtle()
#         self.shape("turtle")
#         color = self.color(color)
#
#         self.penup()
#         pos = self.setpos(x,y)
#
#
#         self.pendown()
#
#
#
#
#
#
#
#
#
# tim  = intialsetup(x=-400 ,y=-300,color="violet")
#
# tim1 = intialsetup(x=-400 ,y=-200,color="indigo")
# tim2 = intialsetup(x=-400 ,y=-100,color="blue")
# tim3 = intialsetup(x=-400 ,y=0,color="green")
# tim4 = intialsetup(x=-400 ,y=100,color="orange")
# tim5 = intialsetup(x=-400 ,y=200,color="red")
# tim6 = intialsetup(x=-400 ,y=300,color="yellow")
#
#
# screen.exitonclick()
