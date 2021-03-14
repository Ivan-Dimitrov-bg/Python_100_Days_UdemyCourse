from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# -----------------------------Label -----------------------------------------
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
# ------------------------------------------Buttons -------------------
def button_click():
    my_label["text"] = "change"
#     or
    my_label.config(text="New Text")

button = Button(text="Click Me", command=button_click)
button.pack()

# -----------------------  Inputs ---------------------
def button2_click():
    new_Text = input.get()
    label2.config(text=new_Text)

label2 = Label(text="I am a Label2", font=("Arial", 24, "bold"))
label2.pack()
input = Entry(width=10)
input.pack()

button2 = Button(text="Modify the label", command=button2_click)
button2.pack()


window.mainloop()
