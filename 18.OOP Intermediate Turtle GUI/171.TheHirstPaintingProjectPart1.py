import turtle as t
import colorgram as co

t.colormode(255)
window = t.Screen()
tim = t.Turtle

image_file = "../18.OOP Intermediate Turtle GUI/spots.jpg"
colors = co.extract(image_file, 20)
l_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    l_colors.append((r, g, b))

print(l_colors)
