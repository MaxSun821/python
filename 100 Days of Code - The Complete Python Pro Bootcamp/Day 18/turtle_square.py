import turtle
from turtle import Turtle, Screen
import random
import colorgram

# t_bag = Turtle()



# for _ in range(20):
#     t_bag.pd()
#     t_bag.forward(15)
#     t_bag.pu()
#     t_bag.forward(15)

# color_list = ["brown", "bisque", "medium spring green", "cornflower blue", "crimson"]
# def draw_shapes(num_size):
#     degree = 360 / num_size
#     for _ in range(num_size):
#         t_bag.forward(100)
#         t_bag.right(degree)
#
# for i in range(3, 10):
#     t_bag.color(random.choice(color_list))
#     draw_shapes(i)

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     color_tuple = (r, g, b)
#     return color_tuple
#
# distribute = [0, 90, 180, 270]

# t_bag.speed(0)
# t_bag.pensize(5)
# for _ in range(100):
#     t_bag.color(random_color())
#     t_bag.forward(30)
#     t_bag.setheading(random.choice(distribute))

# t_bag.speed(0)
#
# def draw_circle(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         t_bag.color(random_color())
#         t_bag.circle(100)
#         t_bag.setheading(t_bag.heading() + size_of_gap)
#
# draw_circle(5)

# colors = colorgram.extract('image.jpg', 20)
# color_list = [(245, 243, 237), (221, 134, 79), (170, 101, 36), (155, 209, 196), (23, 40, 59), (227, 83, 67), (248, 218, 74), (231, 242, 235), (204, 219, 234), (51, 94, 79), (167, 55, 127), (230, 93, 101), (199, 212, 3), (2, 69, 137), (104, 171, 52), (97, 137, 154), (168, 194, 221), (247, 237, 242), (34, 40, 39), (198, 137, 35)]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

# t_bag.penup()
# t_bag.speed(0)
# t_bag.setheading(225)
# t_bag.forward(400)
#
# for i in range(10):
#     t_bag.setheading(0)
#     for _ in range(10):
#         t_bag.dot(20, random.choice(color_list))
#         t_bag.forward(50)
#
#     t_bag.setheading(180)
#     t_bag.forward(500)
#     t_bag.setheading(90)
#     t_bag.forward(50)

# def move_forward():
#     t_bag.forward(10)
#
# def go_back():
#     t_bag.backward(10)
#
# def turn_left():
#     t_bag.left(10)
#
# def turn_right():
#     t_bag.right(10)
#
# def clean_up():
#     t_bag.clear()
#     t_bag.penup()
#     t_bag.home()
#     t_bag.pendown()

my_screen = Screen()
my_screen.setup(width=500, height=400)

# my_screen.listen()
# my_screen.onkey(key='space', fun=move_forward)

# my_screen.onkey(key='w', fun=move_forward)
# my_screen.onkey(key='s', fun=go_back)
# my_screen.onkey(key='a', fun=turn_left)
# my_screen.onkey(key='d', fun=turn_right)
# my_screen.onkey(key='c', fun=clean_up)

is_on_race = False

user_bet = my_screen.textinput(title="Give me your bet", prompt="Enter your bet. Choose a color:")
# print(user_bet)

turtle_color_list = ["red", "blue", "yellow", "pink", "green", "black"]
turtle_list = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(turtle_color_list[turtle_index])
    tim.goto(x=-230, y=(-100 + 40 * turtle_index))
    turtle_list.append(tim)

if user_bet:
    is_on_race = True

while is_on_race:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_on_race = False
            win_color = turtle.pencolor()
            if user_bet == win_color:
                print(f"You've win, the winner color is {win_color}.")
            else:
                print(f"You've lost, the winner color is {win_color}.")
        turtle.forward(random.randint(0, 10))

my_screen.exitonclick()
