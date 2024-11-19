from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.pack()

window.mainloop()
