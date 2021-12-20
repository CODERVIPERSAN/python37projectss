# # object oriented programing
# # _____________________________________________
# # waiter,cook,cashier is class like job v
# # hendry is the waiter ----obj1
# # sandeep is the waiter ---obj2
#
#
# # (object or waiter )= class_name.(attributes or methods)
#
# # object have attributes
# # object do methods
#
# from turtle import Turtle as t
# obj1 = t()
#
#
# from empy import name
#
# obj = name.x
# print(obj)
#
# import empy  # file itself a large space of class
#
# pr = empy.nam()
# print(pr)
# from turtle import Turtle, Screen  ----module
# obj = Turtle()   ------object accessing the class
# my_screen = Screen()  -------object accessing the methods
# my_screen.screensize(600, 600)
# input()


import turtle
# obj = turtle.Turtle()
# obj.shape("turtle")
# obj.color("red")
#
# my_screen = turtle.Screen()
# my_screen.bgcolor("blue")
# for i in range(4):
#     obj.forward(100)
#     obj.left(90)
# my_screen.exitonclick()
# review the turtle module

####################################################################
# pitted table
from prettytable import PrettyTable

table = PrettyTable()
# adding the coulmn
table.add_column("name", ["pikachu", "sandy", "vishnu", "randy orthon"])
table.add_column("data", [98, 56, 90, 45])
table.align = "r"  # change the alignment
print(table)
#pretty table module
#####################################################################
# coffee machine using class as a module
