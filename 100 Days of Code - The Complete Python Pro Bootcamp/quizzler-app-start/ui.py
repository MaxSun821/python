from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzlerInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        self.score_label = Label(self.window, text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.question_canvas = self.canvas.create_text(150, 125,
                                                       font=("Arial", 20, "italic"),
                                                       text="",
                                                       fill=THEME_COLOR,
                                                       width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=15)
        # Button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=true_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_answer)
        self.true_button.grid(row=2, column=1, pady=10)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=false_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_answer)
        self.false_button.grid(row=2, column=0, pady=10)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_canvas, text="You have finished all questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

