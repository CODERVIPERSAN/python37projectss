from tkinter import Tk,Label,Button

tk = Tk()

tk.minsize(width=700, height=500)

tk.config(padx=20, pady=20)

label = Label(text="hello guys welcome to coder vipersan")

# label['text']=""  --- if you need to change the lable then

# label.config(text=)

# place, grid ,pack --- layout manager

label.grid(column=0,row=0)
###################################################
# buttons ----
def func():
    print("button has clicked")

button = Button(text="this is button",command =func)


button.grid(column=1,row=1)

button.config(bg="black",fg="yellow")




tk.mainloop()