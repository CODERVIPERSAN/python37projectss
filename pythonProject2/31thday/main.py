from random import choice
from tkinter import *
from tkinter import messagebox
from pandas import DataFrame, read_csv

CARD_COLOR = "#82B4A0"
count = 0
rand_card = {}

timer_variable = None
BACKGROUND_COLOR = "#66CDAA"

try:
    dataframe = read_csv('./words_to_learn.csv')
except FileNotFoundError:
    dataframe = read_csv('./data/ENGLISH_TAMIL.csv')

data_list = [{row['ENGLISH']: row['TAMIL']} for key, row in dataframe.iterrows()]


# -----------------------------#------------------------
def timer(con):
    global timer_variable
    if con >= 0:
        canvas.itemconfig(time_text, text=f"{con}")
        timer_variable = win.after(1000, timer, con - 1)
        if 0 <= con < 3:
            canvas.itemconfig(card_background, image=back_card)
            canvas.itemconfig(title, text="TAMIL", fill="#FFFFFF")
            global rand_card
            for i in rand_card:
                canvas.itemconfig(word, text=f"{rand_card[i]}", fill="#FFFFFF")

    else:
        canvas.itemconfig(title, fill="black")
        canvas.itemconfig(word, fill="black")
        canvas.itemconfig(card_background, image=front_card)
        start()


def start():
    global rand_card
    try:
        rand_card = choice(data_list)
    except IndexError:
        canvas.itemconfig(title, text="GAME")
        canvas.itemconfig(word, text="OVER")
    else:
        canvas.itemconfig(title, text="ENGLISH")
        for i in rand_card:
            canvas.itemconfig(word, text=i)
        timer(5)


def tick():
    global data_list
    global rand_card

    try:
        data_list.remove(rand_card)
        english_keys = [list(data.keys())[0] for data in data_list]
        tamil_value = [list(data.values())[0] for data in data_list]
        data_dict = {'ENGLISH': english_keys, 'TAMIL': tamil_value}
        data_frame1 = DataFrame(data_dict)
        data_frame1.to_csv("./words_to_learn.csv")
    except ValueError:
        messagebox.showinfo("game over buddy ")
    else:
        reset()


def cross():
    reset()


def reset():
    global timer_variable
    win.after_cancel(timer_variable)
    start()


# ------------------------------------------------
win = Tk()
win.config(padx=20, pady=20, bg=CARD_COLOR)

right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=tick)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=cross)
wrong_button.grid(row=1, column=0)

canvas = Canvas(width=850, height=550)

front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')

card_background = canvas.create_image(425, 275, image=front_card)

canvas.config(bg=CARD_COLOR, highlightthickness=0)
canvas.itemconfig(front_card, padx=20, pady=20, highlightthickness=0)

title = canvas.create_text(427, 150, text="Title", font=('Arial', 30, 'italic'))
word = canvas.create_text(427, 275, text="words", font=('Arial', 50, 'bold'))
# -----------------------------------------------------------------------------------------------------
time_text = canvas.create_text(700, 475, text="00.00", font=('Courier', 30, 'italic'), fill="#FF0000")
canvas.grid(row=0, column=0, columnspan=2)



start()
win.mainloop()
