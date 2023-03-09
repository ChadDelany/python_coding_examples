"""Pong Game"""

# Libraries
from turtle import Screen
from paddle import Paddle

# Setup Screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# Instantiate two paddles.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Keystrokes to control paddle movement.
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Update screen while the game is running.
game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()