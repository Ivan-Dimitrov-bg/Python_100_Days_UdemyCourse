from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 10, "normal")

class State(Turtle):

    def __init__(self, state_name, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.stateName = state_name
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.write(self.stateName,  align=ALIGNMENT, font=FONT)