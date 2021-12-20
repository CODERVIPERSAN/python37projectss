import time
from turtle import Screen, Turtle, turtles
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint
from car_manager import MOVE_INCREMENT, STARTING_MOVE_DISTANCE

screen = Screen()
road = Turtle()
screen.tracer(0)
road.penup()
road.setpos(-280, 280)
road.pendown()
road.forward(600)
road.penup()
road.setpos(-280, -280)
road.pendown()
road.forward(600)
screen.update()
score = Scoreboard()

screen.setup(width=600, height=600)
level = screen.textinput("difficulty level", "0 for easy 1 for medium 2 for difficulty")
screen.tracer(0)
player = Player()
endgame = False

timesleep = 0.1
while not endgame and score.score < 11:
    if level == "0":
        num_game = randint(1, 6)
    elif level == "1":
        num_game = randint(1 + 1, 6)
    elif level == "2":
        num_game = randint(2 + 1, 6)
    print(num_game)
    if score.xcor() < 280:
        score.write(arg=f"score{score.score}", move=True, font=("Courier", 24, "normal"))
    else:
        score.setpos(-280, 280)
    score.clear()

    if num_game == 6:
        car = CarManager()

    for i in turtles()[3::]:
        i.forward(randint(1, STARTING_MOVE_DISTANCE))
        if player.distance(i) < 26:
            endgame = True

    time.sleep(timesleep)
    screen.update()
    screen.listen()
    screen.onkeypress(player.move, "Up")
    boolean = player.finish_line()
    print(boolean)
    if boolean:
        score.clear()
        timesleep = timesleep / 2
        score.increment_score()


else:
    score.setpos(0, 0)
    score.game_over()
screen.exitonclick()
