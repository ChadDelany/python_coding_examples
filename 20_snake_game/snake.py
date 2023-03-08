"""Snake Class"""

# Libraries
from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Initialize Class
    def __init__(self):
        # Create attributes.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create snake method.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segments = Turtle('square')
            new_segments.color('white')
            new_segments.penup()
            new_segments.goto(position)
            self.segments.append(new_segments)

    # Move end of snake to position of snake segment before it (inch-worm movement)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Change direction of snake - up, down, left, right.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


