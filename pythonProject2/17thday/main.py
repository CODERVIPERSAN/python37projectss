from question_model import Question
from data import question_data

score = 0
# question bank
q_lis = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    q_lis += [Question(text, answer)]

# for i in q_lis:
#     print(i.question)
#     user = (input("enter the answer").strip()).capitalize()
#     if i.answer == user:
#         score += 1
#         print("yes correct ", score)
#
#     else:
#         print("no u said wrong ")
#         continue
# print("end of the game",score)       ----by procedural programming

# by oop programming
from quiz_brain import QuizBrain
iam = QuizBrain(q_lis)
iam.question_number = 0
for i in q_lis:
    iam.next_question()
    iam.question_number += 1
    print()
    print()
else:
    print()
    print("u completed the quiz")
    print(f"ur final score {iam.score*100/len(q_lis)}")