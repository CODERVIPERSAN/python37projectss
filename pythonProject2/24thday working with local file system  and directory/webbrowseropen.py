from tkinter import Tk, Button
import webbrowser
root = Tk()
root.title("opening the browser")
root.geometry("600x600")


def google():
    webbrowser.open("www.google.com")


google_open = Button(root,text="click to open google",font=("Arial",24,"bold"),command = google)
google_open.config(fg="black",bg="red",width=20,height=1)
google_open.pack()

root.mainloop()