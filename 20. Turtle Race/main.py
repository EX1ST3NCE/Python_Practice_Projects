# Program to have a race of 6 turtles using turtle module.

from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=600)
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
is_race_on = False

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
y_positions = [-200, -120, -40, 40, 120, 200]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-350, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 360:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You won!! {winning_color} Turtle reached finished line!")
            else:
                print(f"You Lost!! {winning_color} Turtle reached finished line!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
