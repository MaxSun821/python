import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean")
response.raise_for_status()
questions = response.json()

question_data = questions["results"]

# question_data = [
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The scientific name for the Southern Lights is Aurora Australis?",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "Sitting for more than three hours a day can cut two years off a person&#039;s life expectancy.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The commercial UK channel ITV stands for &quot;International Television&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The word &quot;news&quot; originates from the first letters of the 4 main directions on a compass (North, East, West, South).",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The sum of all the numbers on a roulette wheel is 666.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The vapor produced by e-cigarettes is actually water.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The term &quot;Spam&quot; came before the food product &quot;Spam&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "Furby was released in 1998.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
