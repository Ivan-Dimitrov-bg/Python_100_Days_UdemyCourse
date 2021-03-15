from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

RED = "#ac0d0d"
ORANGE = "#f48b29"
YELLOW = "#f0c929"
WHITE = "#fbe6c2"
DEFAULT_EMAIL = "Dimitrov.Ivan.Dimitrov@gmail.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = ([choice(letters) for char in range(randint(8, 10))])
    password_symbols = ([choice(symbols) for symbol in range(randint(2, 4))])
    password_numbers = ([choice(numbers) for number in range(randint(2, 4))])
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    entry_password.insert(0, string=password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def load_data():
    with open("data.json", mode='r') as fileNames:
        data = json.load(fileNames)
    return data

def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {
                    "email": email,
                    "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooops", message="Please be sure you haven't left any fields empty")
    else:
        try:
                data = load_data()
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode='w') as fileNames:
                json.dump(new_data, fileNames, indent=4)
        else:
            with open("data.json", mode='w') as fileNames:
                json.dump(data, fileNames, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def serch_password():
    search_site = entry_website.get()
    try:
        data = load_data()
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Doesn't Exist")
    else:
        if search_site in data:
            entry_password.delete(0, END)
            entry_email.delete(0, END)
            entry_email.insert(0, data[search_site]['email'])
            entry_password.insert(0, data[search_site]['password'])
        else:
            entry_password.delete(0, END)
            entry_email.delete(0, END)
            entry_email.insert(0, DEFAULT_EMAIL)
            entry_password.insert(0, "password is not found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg=WHITE)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)
# ----------------------------------------------------------
#labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# ENTRIES
entry_website = Entry(width=33)
entry_website.grid(column=1, row=1, columnspan=1)
entry_website.focus()

entry_email = Entry(width=45)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, DEFAULT_EMAIL)

entry_password = Entry(width=45)
entry_password.grid(column=1, row=3, columnspan=2)

# BUTTONS
button_generate_password = Button(text="Generate Password",  width=16, command=password_generator)
button_generate_password.grid(column=1, row=4, padx=0, pady=0)

button_add = Button(text="Add", width=9, command=save_password)
button_add.grid(column=2, row=4, columnspan=1, padx=0, pady=0)

button_add = Button(text="Search", width=9, command=serch_password)
button_add.grid(column=2, row=1, columnspan=1, padx=0, pady=0)

window.mainloop()