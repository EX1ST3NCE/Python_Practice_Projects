# Program to make a snake game with turtle module.
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect Collision with Tail
    for parts in snake.snakes[1:]:
        if snake.head.distance(parts) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
