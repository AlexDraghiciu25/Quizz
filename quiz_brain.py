class Quizz_Brain:
    def __init__(self, question):
        self.questions_numbers = 0
        self.question_list = question
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.questions_numbers]
        self.questions_numbers += 1
        user_answer = input(f"Q{self.questions_numbers}: {curr_question.text} (True/False): ")
        self.Check_answer(user_answer, curr_question.answer)

    def still_have_question(self):
        if self.questions_numbers < len(self.question_list):
            return True
        else:
            return False

    def Check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.questions_numbers}")
        print("\n" * 2)