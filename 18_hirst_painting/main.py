"""Generate a Hirst-style Spot Painting"""

import colorgram
import turtle
import random

# Extract colors from the Hirst Spot Painting jpeg.
rgb_colors = []
colors = colorgram.extract('hist_spot_painting.jpg', 30)

# Convert extracted information to list of color tuples.
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# Remove white shades from color extraction.
color_list = rgb_colors[3:]

# Change turtle module color mode.
turtle.colormode(255)

# Instantiate Tim the Turtle.
tim = turtle.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

# Move tim to starting position.
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

# Draw the dots!
for dot_count in range(1, number_of_dots + 1):
    # Draws a row of dots.
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # At end of line, return to next line.
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Keep screen up until mouse click to exit.
screen = turtle.Screen()
screen.exitonclick()
