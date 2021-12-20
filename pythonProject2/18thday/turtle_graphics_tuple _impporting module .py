# python turtle module  to draw graphics
from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color()

import math
for i in range(-500, 500):

    y = 32*math.sin(10*i/20)+32*math.cos(10.5*i/20)
    if i == -500:
        timmy.up()
        timmy.setpos(i,y)
        timmy.down()
    timmy.setpos(i, y)
print(timmy.position())

# for turtle in screen.turtles():
#     # ---screen.turtles returns the attributes for the object
#     print(timmy.color("red"))
#     tommy.forward(90)









screen.exitonclick()
