from turtle import Screen, colormode, turtles, Turtle
from snakeclass import Snake
from foodclass import Food
from scoreclass import Score
import time

referee = Turtle()
referee.color("white")
referee.penup()
referee.setpos(-300, -300)
referee.pendown()
for _ in range(4):
    referee.forward(600)
    referee.left(90)

screen = Screen()
screen.setup(height=700, width=700)
screen.bgcolor("black")
screen.title(titlestring="SWEET SNAKE ")
screen.tracer(0)
colormode(255)

snake = Snake()
food = Food(stretch_len=0.5, stretch_wid=0.5, color="blue")
big_food = Food(stretch_len=2, stretch_wid=2, color="green")
big_food.hideturtle()
score = Score()
screen.listen()
screen.onkeyrelease(snake.up, "Up")
screen.onkeyrelease(snake.down, "Down")
screen.onkeyrelease(snake.right, "Right ")
screen.onkeyrelease(snake.left, "Left")
body = turtles()

endgame = False

while not endgame:

    body[0].speed("fastest")
    body[1].speed("fastest")
    body[2].speed("fastest")
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        score.clear()
        score.score_increment(step=1)

    # detect the collision with wall
    xcor = snake.head.xcor()
    ycor = snake.head.ycor()

    if xcor > 300 or xcor < -300 or ycor > 300 or ycor < -300:
        score.reset()
        snake.reset()

    for segment in snake.body[1:]:
        if snake.head.distance(segment)<10:
                score.reset()
                snake.reset()

    # body[1].setpos(previous)
    # previous = body[1].pos()
    # body[2].setpos(previous)

    screen.update()

    # x = body[0]
    # pos = x.pos()
    # x = pos[0]
    # x+=10

    # body[0].setpos(x,150)

screen.listen()

screen.exitonclick()
