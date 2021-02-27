import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t = Turtle()
t.shape("turtle")
# colors = ["deep sky blue", "red", "tomato", "teal", "olive drab", "dark magenta"]
directions = [0, 90, 270, 360]
t.pensize(15)
t.speed("fastest")
for _ in range(100):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))


