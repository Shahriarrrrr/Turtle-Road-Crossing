from turtle import Turtle, Screen
import time
from player import Player
import random
import cars
import score
import pygame
import winsound

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load('Starting.wav')
red=pygame.mixer.Sound("crash.wav")
pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely
screen = Screen()
screen.setup(900, 600)
Screen().tracer(0)

tim = Player()
scores = score.Score()
screen.listen()
screen.onkey(tim.move, "w")

cars_list = []
cars_manager = cars.Cars()
level = 1
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.create_cars()
    cars_manager.move_cars()

    # Move the cars across the screen
    # for car in cars_list:
    #     car.forward(10 + 8*level)  # Adjust the speed of the cars
    # Remove cars that have gone off-screen
    # cars_list = [car for car in cars_list if car.xcor() > -450]
    for car in cars_manager.all_cars:
        if tim.distance(car) < 20:
            game_is_on = False
            red.play(0, 0, 0)
            pygame.mixer.music.stop()
            scores.game_over()

        elif tim.ycor() > 300:
            tim.goto(0, -250)
            scores.increase_score()
            scores.update_scoreboard()
            level +=1
            cars_manager.increase_level()


screen.exitonclick()

