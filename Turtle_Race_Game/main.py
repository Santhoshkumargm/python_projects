import random
from turtle import Turtle, Screen

screen = Screen()
race_on = False
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race ("
                                                          "red/blue/green/orange/black/brown)? Enter a color:")
colors = ["red", "blue", "green", "orange", "black", "brown"]
x = -450
y = -150
z = 50
turtles = []

if user_bet:
    race_on = True

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += z
    turtles.append(new_turtle)

while race_on:
    for turtle in turtles:

        if turtle.xcor() > 400:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
