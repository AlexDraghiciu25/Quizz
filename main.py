from data import question_data
from question_model import Question
from quiz_brain import Quizz_Brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

quizz = Quizz_Brain(question_bank)

while quizz.still_have_question():
    quizz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quizz.score}/{quizz.questions_numbers}")