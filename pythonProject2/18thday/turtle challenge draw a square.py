# # to draw a square
# challenge 1
# import turtle
#
# my_turt = turtle.Turtle()
# screen = turtle.Screen()
#
#
# def line(pet):
#     pet.forward(100)
#     pet.right(89)
#
#
# for sides in range(4):
#     line(my_turt)
# screen.exitonclick()
#


# to draw a dashed line using turtle
# challenge 2
import turtle

red_turtle = turtle.Turtle()
screen = turtle.Screen()
# for _ in range(30):
#     red_turtle.fd(10)
#     red_turtle.penup()
#     red_turtle.fd(10)
#     red_turtle.pendown()
# screen.exitonclick()
# to draw a each iteration each shape
# sides = 3
# import random
# turtle.colormode(255)
#
#
# def draw(sides):
#     for _ in range(sides):
#         red_turtle.forward(100)
#         red_turtle.right(360 / sides)
#
#
# for sides in range(3, 11):
#     red_turtle.color([random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)])
#     red_turtle.pensize(5)
#     draw(sides)
# screen.exitonclick()


# challenge--4
# random walk
from random import choice, randint


# def left():
#     red_turtle.left(90)
#     red_turtle.forward(20)
#
#
# def right():
#     red_turtle.right(90)
#     red_turtle.forward(20)
#
#
# def forward():
#     red_turtle.forward(20)
#
#
# def backward():
#     red_turtle.backward(20)
#
# turtle.colormode(255)
# choice_list = ["left", "right", "forward", "backward"]
# red_turtle.pensize(10)
# red_turtle.sety(100)
# for _ in range(300):
#     red_turtle.color([randint(0, 255), randint(0, 255),randint(0, 255)])
#     red_turtle.setheading(choice([0, 90, 180 ,270, 360,180]))
#     red_turtle.forward(30)
#     red_turtle.speed("fastest")

# rand_cho = choice(choice_list)
# if rand_cho == choice_list[0]:
#     left()
# elif rand_cho == choice_list[1]:
#     right()
# elif rand_cho == choice_list[2]:
#     forward()
# elif rand_cho == choice_list[3]:
#     backward()
def square(side):
    for _ in range(4):
        red_turtle.fd(side)
        red_turtle.right(90)


# challenge ----5  draw a spirograph
turtle.colormode(255)
for i in range(360//5):
    red_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    red_turtle.speed("fastest")
    square(100)
    # red_turtle.left(7)
    red_turtle.setheading(red_turtle.heading()+5)
screen.exitonclick()
