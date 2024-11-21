from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORDS_FONT = ("Ariel", 60, "bold")

# Read file

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/flash_card_data.csv")
else:
    data_dict = data.to_dict(orient="records")
    current_card = {}


# change word function
def next_word():
    global current_card, wait
    current_card = random.choice(data_dict)
    window.after_cancel(wait)
    canvas.itemconfig(card_canvas, image=card_front_img)
    canvas.itemconfig(language_text, text="German", fill="black")
    canvas.itemconfig(words_text, text=current_card["German"], fill="black")
    wait = window.after(3000, change_card)


def change_card():
    canvas.itemconfig(card_canvas, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(words_text, text=current_card["English"], fill="white")


def remember():
    data_dict.remove(current_card)
    print(len(data_dict))
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv")
    next_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
wait = window.after(3000, change_card)


# Image
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_canvas = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
words_text = canvas.create_text(400, 253, text="", font=WORDS_FONT)

# Button
cross_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=wrong_button_img, command=next_word)
check_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=right_button_img, command=remember)
cross_button.grid(row=1, column=0)
check_button.grid(row=1, column=1)

next_word()


window.mainloop()
