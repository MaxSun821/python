import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.cars_move()

    for car in cars.cars_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.check_goal():
        scoreboard.increase_score()
        player.reset_position()
        cars.level_up()

screen.exitonclick()
