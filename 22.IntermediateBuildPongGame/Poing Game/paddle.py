from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)



    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)





