from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakes = []
x = 0
y = 0
z = 20

for i in range(3):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(x, y)
    x -= z
    snakes.append(snake_segment)

game_is_on = True
while game_is_on:
    for snake_seg in snakes:
        snake_seg.forward(20)









screen.exitonclick()