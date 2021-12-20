from tkinter import *
from file1 import beep
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 60
SHORT_BREAK_MIN = 15
LONG_BREAK_MIN = 30
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def reset():
    global timer
    global rep
    win.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label. config(text="TIMER")
    rep = 0
    beep()


def count_down(count):
    # 00.00

    if count > 0:
        min = count // 60
        sec = count % 60
        if 0 <= sec <= 9:
            sec = f"0{sec}"
        if 0 <= min <= 9:
            min = f"0{min}"
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
        global timer
        timer = win.after(1000, count_down, count - 1)
    else:
        start()


def start():
    global rep
    rep += 1

    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text='LONG BREAK')

    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text='SHORT BREAK')

    else:
        count_down(WORK_MIN * 60)
        label.config(text='ON WORK')

    check_mark.config(text="✔" * (((rep % 8)) // 2))
    beep()


# ---------------------------- UI SETUP ------------------------------- #
# Screen
win = Tk()
win.title(string="POMODORO")
win.config(padx=100, pady=100, bg=PINK)
beep()

#canvas at the center
canvas = Canvas(width=210, height=224, bg=PINK, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')

canvas.create_image(105,112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00.00", fill="black", font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)


label = Label(text='TIMER', font=(FONT_NAME, 30, 'bold'), fg='white', bg="red")
label.grid(row=0, column=1)

start_button = Button(fg='white', text='START', bg='red', font=(FONT_NAME, 15, 'bold'), highlightthickness=0,
                      command=start)
start_button.grid(row=2, column=0)
reset_button = Button(fg='white', text='RESET', bg='red', font=(FONT_NAME, 15, 'bold'), command=reset)
reset_button.grid(row=2, column=2)

check_mark = Label(fg='black', bg=PINK, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(row=3, column=1)
win.mainloop()
