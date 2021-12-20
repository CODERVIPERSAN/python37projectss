import turtle

screen = turtle.Screen()

import pandas

data = pandas.read_csv("./50_states.csv")


def country_data(users_string):
    xcor = int(data[data['state'] == users_string].x)
    ycor = int(data[data['state'] == users_string].y)
    country = list(data[data['state'] == users_string].state)
    country = country[0]
    return country, xcor, ycor
def check(guess):
    for i in list(data.state):
        if i == guess:
            return True
    return False



screen.title("us states game")
img = "./blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
endgame = False
number_of_country = 0
score = 0
all_states = list(data.state)
guessed_states=[]
guess=" "
while not endgame and score <= 50:
    if guess == 'Exit':
        lis_not_guessed=[ state for state in all_states if state not in guessed_states]
        data = pandas.DataFrame(lis_not_guessed)
        data.to_csv("./notguessed.csv")

        break

    if number_of_country == 50:
        guess = screen.textinput("guess_country", "guess here")
    else:
        guess =screen.textinput(f"{score}/50  remains--{number_of_country}","guess here")
    guess = (guess.strip()).title()
    if check(guess=guess):
        new_turtle = turtle.Turtle()
        new_turtle.setpos(country_data(guess)[1],country_data(guess)[2])
        new_turtle.write(arg=f"{guess}")
        guessed_states.append(guess)
        score += 1




    number_of_country+=1






# def mouse_click(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(mouse_click)
# screen.mainloop()
# screen.exitonclick()
