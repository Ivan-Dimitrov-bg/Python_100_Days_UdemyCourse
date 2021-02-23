# from data import question_data
from dataTrivia import question_data
from question_model import Qustion
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Qustion(text=question_text, answer=question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")