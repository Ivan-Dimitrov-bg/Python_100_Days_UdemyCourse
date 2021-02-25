from turtle import Turtle, Screen
import random
t = Turtle()
# t.shape("turtle")
colors = ["deep sky blue", "red", "tomato", "teal", "olive drab", "dark magenta"]
directions = [0, 90, 270, 360]
t.pensize(15)
t.speed("fastest")
for _ in range(100):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheading(random.choice(directions))



# window.exitonclick()
