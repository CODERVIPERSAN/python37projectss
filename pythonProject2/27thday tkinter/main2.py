from tkinter import Tk, Label, Entry, Button, Scale, IntVar, Radiobutton

screen = Tk()
screen.title("MILE TO KM CONVERTER")
screen.minsize(width=100, height=100)


def padding(self, num1, num2):
    self.config(padx=num1, pady=num2)


def radio():
    if var.get() ==1:
        scale_1()

    elif var.get() ==2:
        button_1()

var = IntVar()

radio1 = Radiobutton(variable=var, text='access the slider', value=1, command=radio)
radio2 = Radiobutton(variable=var, text='access the entry', value=2, command=radio)
radio1.grid(row=2, column=2)
radio2.grid(row=3, column=2)

padding(screen, 10, 10)

label1 = Label(text='miles', font=('Arial', 10, 'bold'))
label1.grid(row=0, column=2)
padding(label1, 5, 5)

label2 = Label(text='kilometer', font=('Arial', 10, 'bold'))
label2.grid(row=1, column=2)
padding(label2, 5, 5)
label_km = Label(text='0', font=('Arial', 10, 'bold'))
label_km.grid(row=1, column=1)
padding(label_km, 5, 5)
label_equal_to = Label(text='equal to', font=('Arial', 10, 'bold'))
Font = 'Arial', 10, 'bold'
label_equal_to.grid(row=1, column=0)
padding(label_equal_to, 5, 5)

entry = Entry(width=10)

entry.grid(row=0, column=1)

def mile_km():
    mile = float(entry.get())
    km = 1.60934 * mile
    label_km.config(text=str(km))

def button_1():
    button = Button(text='CALCULATE', command=mile_km)
    button.grid(row=2, column=1)

def scale_com(value):
    mile = float(value)
    km = mile * 1.60934
    label_km['text'] = str(km)

def scale_1():
    scale = Scale(from_=0, to=100000, command=scale_com)
    scale.grid(row=0, column=0)

screen.mainloop()
