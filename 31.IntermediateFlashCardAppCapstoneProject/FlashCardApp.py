from tkinter import *
from tkinter import messagebox
import json
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
SECONDS_WAIT = 3
random_word = {}
timer = None
data = None
data_dict = None
# ---------------------------- FUNCTIONALITY --------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = pandas.DataFrame.to_dict(data, orient="records")

def pick_random_card():
    global random_word, timer
    random_word = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word_title, text=f"{list(random_word.keys())[0]}")
    canvas.itemconfig(word_text, text=f"{list(random_word.values())[0]}", fill="black")
    timer = window.after(3000, func=show_answer)

def button_right_click():
    global timer, data, random_word
    window.after_cancel(timer)
    data_dict.remove(random_word)
    new_data_dict = data_dict
    new_data = pandas.DataFrame(new_data_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    pick_random_card()



def button_wrong_click():
    global timer
    window.after_cancel(timer)
    pick_random_card()


def show_answer():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word_title, text=f"{list(random_word.keys())[1]}")
    canvas.itemconfig(word_text, text=f"{list(random_word.values())[1]}", fill="white")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(10000, func=show_answer)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
word_title = canvas.create_text(400, 150, text="Title", fill="Black", font=("Ariel", 35, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="Black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, command=button_right_click, highlightthickness=0)
button_right.grid(column=0, row=1)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, command=button_wrong_click, highlightthickness=0)
button_wrong.grid(column=1, row=1)

pick_random_card()

window.mainloop()