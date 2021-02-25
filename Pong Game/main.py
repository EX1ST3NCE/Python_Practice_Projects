from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(x=550, y=0)
l_paddle = Paddle(x=-550, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Top and Bottom walls
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Detect collision with Right Wall
    if ball.xcor() > 580:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Detect collision with Left Wall
    if ball.xcor() < -590:
        ball.reset_position()
        scoreboard.increase_r_score()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 520 or ball.distance(l_paddle) < 50 and ball.xcor() < -520:
        ball.bounce_x()

screen.exitonclick()
