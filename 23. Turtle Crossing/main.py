from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=800)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
