from tkinter import *

window = Tk()
window.config(height=500, width=500)
window.config(padx=30, pady=30)

entry_m = Entry()
entry_m.focus()
entry_m.grid(column=1, row=0)

entry_k =Entry()
entry_k.grid(column=1, row=1)

label_m = Label(text="Miles")
label_m.grid(column=2, row=0)

label_k = Label(text="Km")
label_k.grid(column=2, row=1)

lable = Label(text="is equal to")
lable.grid(column=0, row=1)

def button_click():
    m_value = float(entry_m.get())
    k_value = m_value * 1.609344
    entry_k.insert(END, string=k_value)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()