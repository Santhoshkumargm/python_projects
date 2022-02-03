import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.hideturtle()
angle = 5
x = 360 / angle
for i in range(int(x)):
    tim.speed(0)
    tim.color(random_color())
    tim.circle(80)
    current_heading = tim.heading()
    tim.setheading(current_heading + angle)
    tim.tiltangle(angle)

my_screen = t.Screen()
my_screen.exitonclick()
