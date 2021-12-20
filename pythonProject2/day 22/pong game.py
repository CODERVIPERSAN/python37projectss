import turtle
from turtle import Turtle, Screen, turtles,colormode
from paddleclass import Paddle
import random
from ballclass import Ball
import time
from scoreclass import Score

screen = Screen()

screen.setup(width=1200, height=600)
refree = Turtle()
score1 = Score(90)
score2 = Score(-90)
refree.color("white")
refree.speed("fastest")
refree.penup()
refree.setpos(-600,-300)
refree.pendown()
for _ in range(2):
    refree.forward(1200)
    refree.left(90)
    refree.forward(600)
    refree.left(90)
refree.forward(600)
refree.left(90)
dis = 600
while dis:
    refree.speed("fastest")
    refree.forward(10)
    refree.penup()
    refree.forward(10)
    refree.pendown()
    dis-=20

screen.bgcolor("black")

screen.title("THE PONG GAME ")
screen.tracer(0)
colormode(255)
# CREATE AND MOVE THE PADDLE
###########################################
paddle = Paddle(position_of_paddle=(550, 0), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
paddle1 = Paddle(position_of_paddle=(-550, 0), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
ball = Ball()
screen.listen()
screen.onkeypress(paddle.move_front, "Up")
screen.onkeypress(paddle.move_back, "Down")
screen.onkeypress(paddle1.move_front,"q")
screen.onkeypress(paddle1.move_back,"a")
############################################
endgame = False
while not endgame:
    time.sleep(0.1)
    ball.move()
    ball.bounce()
    paddle_ycor = paddle.ycor()
    paddle1_ycor = paddle1.ycor()
    ball_ycor = ball.ycor()
    if abs(paddle_ycor - ball_ycor) <55 and abs(paddle.xcor()-ball.xcor()) == 30:
        ball.x_move *= -1
    if abs(paddle1_ycor - ball_ycor) < 55 and abs(paddle1.xcor() - ball.xcor()) == 30:
        ball.x_move *= -1
    if ball.xcor()>600:
        score1.clear()
        score1.score_increment()
        ball.reset_position()

        time.sleep(1)
    elif ball.xcor()<-600:
        score2.clear()
        score2.score_increment()
        ball.reset_position()
        time.sleep(1)

    if score1.score>11:
        score1.game_over("player 1  ")
        endgame= True
    elif score2.score>11:
        endgame = True
        score2.game_over("player 2")


    screen.update()




# tur_list = []
# for i in range(-40, 60, 20):
#     tur = Turtle()
#     tur.penup()
#
#     tur.shape("square")
#     tur.color("white")
#     tur.setpos(350, i)
#     tur_list += [tur]
#
#
# def forward(angle):#     for i in tur_list:
#         i.setheading(angle)
#     i.forward(20)
#
#
# screen.listen()
# screen.onkeypress(forward(90), "Up")
# screen.onkeypress(forward(-90), "Down")

screen.exitonclick()

