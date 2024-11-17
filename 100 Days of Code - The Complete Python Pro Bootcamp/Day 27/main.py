import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)

# Label
my_label = tkinter.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_label.pack()
window.mainloop()
