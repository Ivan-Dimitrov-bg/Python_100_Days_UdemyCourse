from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# -----------------------------Label -----------------------------------------
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))


my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=30)
# ------------------------------------------Buttons -------------------
def button_click():
    my_label["text"] = "change"
#     or
    my_label.config(text="New Text")

button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)


entry = Entry()
entry.grid(column=3, row=2)

buttonTwo = Button(text="New Button")
buttonTwo.grid(column=2, row=0)

window.mainloop()