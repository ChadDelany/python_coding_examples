# Turtle GUI project
from turtle import Turtle, Screen
import random

tim = Turtle()

# '''Draw a Red Turtle, Move Forward, and Turn Right
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# '''Draw a Square'''
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# '''Import a new non-standard library'''
# import heroes
# print(heroes.gen())

# '''Draw a Dashed Line.
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# '''Initial nested for loops for nested polygons (see next solution)'''
# for num_sides in range(3,11):
#     for sides in range(num_sides):
#         angle = 360 / sides
#         tim.forward(100)
#         tim.right(angle)

# '''Drawing Nested Polygons in Random Colors'''
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

'''Generate a Random Walk'''









screen = Screen()
screen.exitonclick()
