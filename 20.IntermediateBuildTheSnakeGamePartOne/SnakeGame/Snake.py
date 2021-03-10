from turtle import Turtle
MOVE_DISTANCE = 20
class Snake:
    segments = []
    def __init__(self):
        for i in range(1, 4):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=0 - (i * 20), y=0)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def down(self):
        self.segments[0].setheading(270)