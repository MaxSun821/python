from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORDS_FONT = ("Ariel", 60, "bold")


# change word function
def change_word():
    word = random.choice(data["German"])
    canvas.itemconfig(words_text, text=word)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Read file
data = pandas.read_csv("./data/flash_card_data.csv")

# Image
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")
right_button_img = PhotoImage(file="./images/right.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text
language_text = canvas.create_text(400, 150, text="German", font=LANGUAGE_FONT)
words_text = canvas.create_text(400, 253, text=random.choice(data["German"]), font=WORDS_FONT)

# Button
cross_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=wrong_button_img, command=change_word)
check_button = Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=right_button_img, command=change_word)
cross_button.grid(row=1, column=0)
check_button.grid(row=1, column=1)


# print(data)
# print(type(data["German"].values[0]))

window.mainloop()
