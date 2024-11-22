import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(current_question.text)
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        q_list_length = len(self.question_list)
        if self.question_number == q_list_length:
            return False
        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    def complete_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")
