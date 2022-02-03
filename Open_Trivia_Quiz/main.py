from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []
for x in range(len(question_data)):
    new_question = Question(question_data[x]["question"], question_data[x]["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


