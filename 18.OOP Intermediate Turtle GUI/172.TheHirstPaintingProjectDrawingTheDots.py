import turtle as t
import random
import colorgram as co

t.colormode(255)
window = t.Screen()
tim = t.Turtle()

l_colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71)]
counter = 0

def set_start_position():
    tim.penup()
    tim.setx(-200)
    tim.sety(-200)
    tim.down()

set_start_position()

for i in range(1, 11):

    tim.penup()
    tim.sety(tim.position()[1] + 50)
    tim.setx(-200)

    for _ in range(10):
        tim.dot(20, random.choice(l_colors))
        counter += 1
        tim.forward(50)


tim.hideturtle()

window.exitonclick()