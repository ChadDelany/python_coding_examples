""""Snake Game"""

from turtle import Screen, Turtle

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Constructing the 'snake'
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)




screen.exitonclick()
