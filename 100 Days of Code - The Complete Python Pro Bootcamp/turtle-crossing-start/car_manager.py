from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            random_y = random.randint(-230, 250)
            car.color(random.choice(COLORS))
            car.goto(300, random_y)
            self.cars_list.append(car)

    def cars_move(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
