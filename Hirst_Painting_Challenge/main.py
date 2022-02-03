# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst_dots.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as t
t.colormode(255)

tim = t.Turtle()
x = -225
y = -225
z = 50
color_list = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

tim.hideturtle()
tim.speed(0)
for i in range(10):
    tim.penup()
    tim.goto(x, y)
    tim.pendown()
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    y += z

screen = t.Screen()
screen.exitonclick()
