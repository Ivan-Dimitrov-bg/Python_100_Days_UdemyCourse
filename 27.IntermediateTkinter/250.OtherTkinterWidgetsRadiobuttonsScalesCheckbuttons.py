from tkinter import *

screen = Tk()
screen.title("My First GUI Program")
screen.minsize(width=500, height=300)

#-----------Entries----------
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
#get text
print(entry.get())
entry.pack()

#-----------Text--------
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multiple line entries")
print(text.get("1.0", END))  #  starting from the first line at position zero
text.pack()

#-------------spin box-------
def spinbox_used():
    #get the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# ----------------Scale ----------------
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# ----------Checkbutton---------
def checkbutton_used():
    # Print 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#--------------RadioButtons-------------

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#------------------Listbox---------------
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



screen.mainloop()