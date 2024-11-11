import random

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for item in question_data:
    questions_bank.append(Question(item['question'], item['correct_answer']))

# print(questions_bank)

quiz = QuizBrain(questions_bank)
while quiz.still_has_question():
    quiz.next_question()

quiz.complete_quiz()
