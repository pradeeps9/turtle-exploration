from turtle import *
import random

# Setting color to RGB
Screen().colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


tim = Turtle()
tim.pensize(5)

# moving direction
move_ang = [0, 90, 180, 270]

for _ in range(500):
    tim.pencolor(change_color())
    tim.setheading(random.choice(move_ang))
    tim.forward(40)
