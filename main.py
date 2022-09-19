from question_model import Question
from data import question_data
from quiz_mechanics import QuizMechanics

question_bank = []
for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
                            # https://bobbyhadz.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str
    question_bank.append(new_question)

# |test| print(question_bank[0].text, question_bank[0].answer)
         # this taps into element 0 keys "text" and "answer" and prints their respective values

quiz = QuizMechanics(question_bank)

quiz.welcome()
while quiz.keep_asking() is True: # or: while quiz.keep_asking():  # or: for i in range(len(question_bank)):
    quiz.next_question()
else:
    quiz.final_score()
