"""Turtle Crossing Game"""

# Libraries
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects from classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Setup keystroke input
screen.listen()
screen.onkey(player.go_up, 'Up')

# Run game
game_is_on = True
while game_is_on:
    # Setup game refresh speed
    time.sleep(0.1)
    screen.update()

    # Generate cars.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Close screen on mouse click.
screen.exitonclick()
