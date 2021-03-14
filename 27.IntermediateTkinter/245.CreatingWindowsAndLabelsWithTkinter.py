import tkinter

window = tkinter.Tk()

window.title("My first GUI program")

window.minsize(width="500", height="300")

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

my_label.pack(side="left", expand=1)







window.mainloop()