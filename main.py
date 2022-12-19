from data import question_data
from question import Question
from quiz import Quiz_brain
from ui import *
question_bank=[]
for a in question_data:
    b= a["question"]
    answer=a["correct_answer"]
    new_question= Question(b,answer)
    question_bank.append(new_question)
new_obj=Quiz_brain(question_bank)
obj=GraphicInterface(new_obj)
#while new_obj.still_has_questions():
    #new_obj.next_question()














































































