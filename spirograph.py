from turtle import *

# Draw a Spirograph
tim = Turtle()
tim.speed(0)

def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        tim.pencolor(change_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

