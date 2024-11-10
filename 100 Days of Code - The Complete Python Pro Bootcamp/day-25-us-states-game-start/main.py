import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_count = 0
states_list = []

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
states_dict = {
    "state": all_states
}

while correct_count < 50:
    answer_state = turtle.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in states_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    data_coordinate = data[data.state == answer_state]
    if answer_state in all_states:
        if answer_state not in states_list:
            states_list.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(data_coordinate.x.item(), data_coordinate.y.item())
            t.write(answer_state)
            correct_count += 1

