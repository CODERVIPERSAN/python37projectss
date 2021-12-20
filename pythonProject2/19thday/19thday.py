from turtle import Turtle, Screen

reddy = Turtle()
win = Screen()


# project we are working turtle race and etch a sketch
##############################################################
# turtle event listeners
# key listening is event listener


def forward():
    reddy.speed("fastest")
    reddy.fd(10)

def backward():
    reddy.speed("fastest")
    reddy.backward(10)


def anticlockwise():
    reddy.speed("fastest")
    new_heading = reddy.heading() - 10
    reddy.seth(new_heading)


def clockwise():
    reddy.speed("fastest")
    heading = reddy.heading()+10
    reddy.seth(heading)
def clear():
    reddy.penup()
    reddy.clear()
    reddy.home()
    reddy.pendown()


win.onkeypress(fun=forward, key="Up")
win.onkeypress(fun=backward, key="Down")
win.onkeypress(fun=clockwise, key="Left")
win.onkeypress(fun=anticlockwise, key="Right")
win.onkey(fun=clear,key="c")
# win.onkeyrelease(fun=)
# -- as the input  as a parameter
# we pass only a name of the function not the parenthesis
win.listen()
win.exitonclick()

# add the value of a and b and subtract it with value 5

# good example for the function as a parameter
# def add(a, b):
#     return a+b
#
#
# def subtract(value_add):
#     return value_add(int(input("enter a")),int(input("enter b"))) - 5
#
#
# print(subtract(add))
