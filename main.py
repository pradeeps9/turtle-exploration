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
    
