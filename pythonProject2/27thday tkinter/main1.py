from tkinter import Tk, Label, Button, Entry, Text, END, Spinbox, Scale, Checkbutton, IntVar, Radiobutton, Listbox

tk = Tk()
tk.minsize(width=700, height=500)
tk.title("coder vipersan")
tk.config(padx=20, pady=20)
label = Label(text="hello guys welcome to coder vipersan", font=("Arial", 10, "bold"))

# python arguments **kwargs
# advanced python arguments
label['text'] = 'new text'
label.config(text='no command received so far ')
# label.place(x=100,y=0)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)


################################################################
# buttons


def button_clicked():
    here = entry.get()
    label.config(text=f"{here}")


button = Button(text='Click me', command=button_clicked)
button['fg'] = 'red'
button['bg'] = 'black'
button.grid(column=1, row=1)
button.config(padx=50, pady=50)

# new_button
new = Button(text='new_click')
new.grid(row=0, column=2)

# Entry
entry = Entry()
entry.insert(index=END, string='enter something here ')
# entry['width'] = 20
# entry['font'] = ('Arial', 10, 'italic')
entry.config(width=20, font=('Arial', 10, 'italic'))
entry.grid(column=3, row=2)
###########################
entry.get()  # to get output
#################################


# next
# text box
text = Text(height=10, width=50)
text.focus()  # to focus first
text.insert(END, chars="enter something in the text box")
text.get('1.0', END)
text.place(x=10, y=300)


#####################################################################
# spinbox
def spin():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=100, width=10, command=spin)


# ##################################################
# scale slider
def s_cale(value):
    print(value)


scale = Scale(from_=0, to=100, command=s_cale)

# check box

on_off = IntVar()


def com():
    if on_off.get() == 1:
        scale.grid(column=5, row=5)
    else:
        scale.config(column=None, row=None)


checkbox = Checkbutton(text='check this for verification', variable=on_off, command=com)


# checkbox.grid(row=4,column=4)

# Radio button
def radio():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1', variable=radio_state, command=radio, value=1)
radiobutton2 = Radiobutton(text='option2', variable=radio_state, command=radio, value=2)
radiobutton1.grid(row=4, column=4)
radiobutton2.grid(row=5, column=5)


# list box
def listbox_used(event):
    print(list_box.get(list_box.curselection()))


list_box = Listbox(height=4)
fruits_list = ['apple', 'mango', 'banana', 'strawberry']
for fruit in fruits_list:
    list_box.insert(fruits_list.index(fruit), fruit)
list_box.bind('<<ListboxSelect>>', listbox_used)
list_box.grid(row=4, column=5)
tk.mainloop()
########################################################
# layout  manager
# pack # place #grid

# pack doesn't defines the position just pack each of the widget
# place ---precision positioning
