from turtle import *
import random

tim = Turtle()

tim.shape('arrow')
tim.shapesize(0.5)
tim.color('red')
tim.forward(100)
tim.right(90)


#  Drawing a Dashed line
for x in range(15):
    tim.pd()
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()
    
    
# Draw shapes from triangle to decagon
no_of_sides = 3
colours = ["royal blue", "teal", "firebrick", "dark orchid", "orange red", "green yellow", "crimson", "midnight blue", ]
# Setting up turtle
tim.penup()
tim.left(135)
tim.forward(100)
tim.right(135)
tim.pendown()

# Going to position to draw shapes
Setting (X,Y)
tim.setx(-100)
tim.sety(100)

# Starting to draw shapes 
for _ in range(3, 11):
    angle = 360 / no_of_sides
    tim.color(random.choice(colours))

    for _ in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)

    no_of_sides += 1

