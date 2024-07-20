from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain
question_bank=[]
for item in question_data:
    question_bank.append(QuestionModel(item['question'],item['correct_answer']))

quiz=QuizBrain(question_bank)

for questions in range (len(question_bank)):
    ans=quiz.nextQuestion()
    res=quiz.checkAnswer(ans)
