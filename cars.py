import turtle
import random
import time

COLORS = ["red", "blue", "purple", "black", "yellow", "orange", "green"]
MOVES = 5



class Cars:
    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5

    def create_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = turtle.Turtle()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.left(180)
            new_car.goto(400, random.randint(-230, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.starting_move_distance)

    def increase_level(self):
        self.starting_move_distance+=MOVES


