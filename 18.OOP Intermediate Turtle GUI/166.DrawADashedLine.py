#Importing the module
import turtle

#The turtle creation
p = turtle.Turtle()
p.shape("turtle")
p.color("black")

for _ in range(1, 10):
    p.penup()
    p.forward(10)
    p.pendown()
    p.forward(10)

window = turtle.Screen()
window.exitonclick()
