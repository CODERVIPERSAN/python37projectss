#colorgram
import turtle
import colorgram
import random

from turtle import Turtle,Screen
pet = Turtle()
screen = Screen()
turtle.colormode(255)
# turtle.colormode(255)
# by using colorgram extract the color from the image
rgb_colors = []
colors = colorgram.extract(r"C:\Users\Santhosh R\PycharmProjects\100daysofcode_angela_yu\18thday\OIP.jpg",15)
for color in colors:
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

rgb_colors = [(198, 165, 114), (144, 80, 54), (218, 201, 140), (57, 93, 121), (165, 151, 49), (132, 33, 22), (135, 160, 179), (74, 36, 28), (50, 116, 87), (195, 93, 75), (147, 176, 149)]

pet.hideturtle()
def line():
    for _ in range(10):
        pet.color(random.choice(rgb_colors))
        pet.dot(20)
        pet.penup()
        pet.forward(50)
        pet.pendown()


for y in range(-300,200,50):
    pet.speed("fastest")
    pet.penup()
    pet.setpos(-200, y)
    pet.pendown()
    line()







screen.exitonclick()