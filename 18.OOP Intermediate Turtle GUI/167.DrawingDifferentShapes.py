from turtle import Turtle, Screen
import random
t = Turtle()
t.shape("turtle")
colors = ["deep sky blue", "red", "tomato", "teal", "olive drab", "dark magenta"]

for number_of_sides in range(3, 10):
    t.color(random.choice(colors))
    for _ in range(number_of_sides):
        t.forward(100)
        t.left(360/number_of_sides)


# window.exitonclick()
