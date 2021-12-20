from tkinter import *
# message box
from tkinter import messagebox

from pyperclip import copy

from pypassword import passwordfunc
from json import dump, dumps, load, JSONDecodeError


# import pandas
#
# web_list = []
# pass_list = []
# email_list = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def py_password():
    password_entry.delete(0, END)
    password = passwordfunc()
    password_entry.insert(index=END, string=password)
    copy(password)


# z1iG)L20$(i0!5x1dj0(RE%33&n&WeH&R(nL5MSN
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    # global email_list
    # global pass_list
    # global web_list
    info = f"{website_entry.get()}|{email_entry.get()}|{password_entry.get()}\n"
    filename = "data.txt"
    w = website_entry.get()
    p = password_entry.get()
    length_web = len(w.strip())
    length_pass = len(p.strip())
    if not(length_pass and length_web):
        messagebox.showerror(title="Error", message="please give some inputs")
        return
    # if not length_web:
    # messagebox.showerror(title="Error", message="please give some inputs")
    # return
    is_ok = messagebox.askokcancel(title="conformation",
                                   message=f"Are you ready to sent the details****{info}***** to the "
                                           f"file with filename *****{filename}*****")
    if is_ok:
        data_dict = {
            website_entry.get(): {
                'email': email_entry.get(),
                'password': password_entry.get()
            }
        }
        with open(filename, "a") as file:
            file.write(info)
        ############################################json file
        try:
            with open('data.json', "r") as file_name:
                # read
                data = load(file_name)
                # update
                data.update(data_dict)
        except JSONDecodeError:
            with open('data.json', 'w') as file:
                dump(data_dict, file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                dump(data_dict, file, indent=4)
        else:
            with open('data.json', 'w')as file_name:
                dump(data, file_name, indent=4)


############################################################
# web_list += [website_entry.get()]
# pass_list += [password_entry.get()]
# email_list += [email_entry.get()]
# data_dict = {'website': web_list, 'email': email_list, 'password': pass_list}
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")


def clear():
    # global pass_list, email_list, web_list
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, email_entry.get().index('@'))


def search():
    entry = (website_entry.get()).strip()
    try:
        with open('data.json') as file:
            data_dict = load(file)
    except JSONDecodeError:
        messagebox.showinfo(title="result on you search", message="no data in the file add some data ")
    except FileNotFoundError:
        messagebox.showinfo(title='result on you search', message="add json file first add and create the data ")
    else:
        for data in data_dict:
            if data == entry:
                print(data_dict[entry])
                messagebox.showinfo(title=f"you search is successful",
                                    message=f"\nwebsite email\t{data_dict[data]['email']},\nwebsite pass word\t{data_dict[data]['password']} ")
                break
        else:
            messagebox.showinfo(title="search", message=f"not details added for  {entry}")


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title(string="PASSWORD MANAGER")

win.config(padx=100, pady=100)
canvas = Canvas(width=200, height=200)
photo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_img)
canvas.itemconfig(photo_img, padx=20, pady=0)
canvas.grid(row=0, column=1)
FONT = ('Arial', 20, 'italic')

# label section
website_label = Label(text='Website', font=FONT)
website_label.config(padx=10, pady=10)
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username', font=FONT)
email_label.config(padx=10, pady=10)
email_label.grid(row=2, column=0)

password_label = Label(text='Password', font=FONT)
password_label.config(padx=10, pady=10)
password_label.grid(row=3, column=0)

# entry box

website_entry = Entry(width=33, font=('Arial', 15, 'normal'))
website_entry.insert(index=END, string="enter the website here")
website_entry.focus()
website_entry.grid(row=1, column=1)
#
email_entry = Entry(width=50, font=('Arial', 15, 'normal'))
email_entry.insert(index=END, string="santhoram2002@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=33, font=('Arial', 15, 'normal'))
password_entry.insert(index=END, string="paste the password")
password_entry.grid(row=3, column=1)

# button
generate_button = Button(text="Generate Password", width=25, fg="white", bg="black", command=py_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=80, fg="white", bg="black", command=add_data)
add_button.grid(row=4, column=1, columnspan=2)
clear_button = Button(text="clear", width=10, fg="white", bg="black", command=clear)
clear_button.grid(row=0, column=2)
search_button = Button(text="search", width=15, fg="white", bg="black", command=search)
search_button.grid(row=1, column=2)
win.mainloop()
