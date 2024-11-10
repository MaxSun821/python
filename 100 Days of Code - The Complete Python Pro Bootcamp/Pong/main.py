from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


my_screen = Screen()
my_screen.title("Pong Game")
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.listen()
my_screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


my_screen.onkey(r_paddle.up, "Up")
my_screen.onkey(r_paddle.down, "Down")

my_screen.onkey(l_paddle.up, "w")
my_screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

my_screen.exitonclick()
