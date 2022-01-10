from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -70
race_is_on = False

for clr in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[clr])
    new_turtle.pu()
    new_turtle.goto(-230, y)
    all_turtles.append(new_turtle)
    y += 30

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print(f"You won {turtle.pencolor()} turtle won the race.")
            else:
                print(f"You lost. {turtle.pencolor()} turtle won the race. ")
            race_is_on = False

        random_dis = random.randint(0, 10)
        turtle.forward(random_dis)

screen.exitonclick()
