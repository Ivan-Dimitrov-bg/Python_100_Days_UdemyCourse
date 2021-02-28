from turtle import Turtle, Screen

import random

is_race_start = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet",
                              prompt=f'Enter the color of the turtle you think will run the race:'
                                     f' (red,orange,yellow,green,blue,purple):')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtule = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-130 + (int(i) * 50))
    all_turtule.append(new_turtle)

if user_input:
    is_race_start = True

winning_color = ""
while user_input:
    for turtle in all_turtule:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            user_input = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

if winning_color == user_input:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()