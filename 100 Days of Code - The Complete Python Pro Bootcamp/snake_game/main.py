from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_screen.listen()

snake = Snake()
food = Food()
score_board = ScoreBoard()


my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.get_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        snake.reset()

    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            snake.reset()



my_screen.exitonclick()
