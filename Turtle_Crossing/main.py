import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
### SCREEN ###
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
### PLAYER TURTLE ###
player = Player()
### SCOREBOARD ###
scoreboard = Scoreboard()
### Car Manager ###
car_manager = CarManager()
### Screen Listener ###
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.025)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # When turtle successfully crosses to the end
    if player.ycor() >= 280:
        player.restart()
        scoreboard.update_scoreboard()
        car_manager.level_up()
    # Collision with cars
    for car in car_manager.all_cars:                # Loops through all the cars
        if car.distance(player) < 20:               # Compares each box's distance to player
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()