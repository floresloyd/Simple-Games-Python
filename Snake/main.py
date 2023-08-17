from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
### SCREEN / GUI ####
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Classic')
screen.tracer(0)                                                 # Turns off animation. Partnered with update - Line 26
### GAME VARIABLES ###
snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()                                               # REFRESHES SCREEN FOR FLUID MOVEMENT
    time.sleep(0.1)                                               # 1-second delay on screen
    snake.move()
    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()
    # Detecting collision with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # Detecting if snake collides with any of its segments/tail:
    for segment in snake.snake_segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
