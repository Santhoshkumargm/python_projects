from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
x = len(question_data)
for i in range(x):
    new_question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    final_score = quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
