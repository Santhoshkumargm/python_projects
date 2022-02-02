class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} True/False: ")
        current_question_answer = current_question.answer
        self.check_answer(current_question_answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, q_answer, u_answer):
        if q_answer.lower() == u_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


