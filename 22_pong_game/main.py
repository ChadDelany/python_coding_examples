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

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()