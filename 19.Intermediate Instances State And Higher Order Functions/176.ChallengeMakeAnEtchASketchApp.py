# W = Forword
# S = Backward
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")
def move_fowerd():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def turn_left():
    tim.left(90)

def turn_right():
    tim.right(90)


def move_counter_clockwise():
    tim.circle(90, 100.00)

def move_clockwise():
    tim.circle(-90, 100.00)

def clear_drawing():
    tim.reset()
    #tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_fowerd)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()

