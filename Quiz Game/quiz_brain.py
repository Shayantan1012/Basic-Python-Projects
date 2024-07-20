class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0;
        self.q_list=q_list
        self.score=0
        
    def nextQuestion(self):
        current_question=self.q_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.question} (True/False): ").lower()
        self.question_number+=1
        if(user_answer=='true'):return 'True'
        else :return 'False'
    def checkAnswer(self,user_ans):
        current_question=self.q_list[self.question_number]
        if(user_ans==current_question.ans):
            self.score+=1;
            print("Your Answer is correct!!!")
        else :print("Your Answer is not correct!!!")
        print(f'Your current score is->{self.score}/{len(self.q_list)}')
            