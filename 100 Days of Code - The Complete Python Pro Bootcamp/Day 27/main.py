import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)

# Label
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)


entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
