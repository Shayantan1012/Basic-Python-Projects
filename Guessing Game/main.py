from art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check(guess,answer,turns):
    if(guess<answer):
        print("Too High!!!")
        return turns-1;
    elif(guess>answer):
        print("Too Low!!!")
        return turns-1;
    else:
        print(f"You got it! The answer was {answer}.")  
        return 0  


def setDificulty():
    difi=input("Give your Difficulty Level in 'easy' and 'hard !!!->").lower()
    if(difi=='easy'):
        return EASY_LEVEL_TURNS
    elif(difi=='hard'):
        return HARD_LEVEL_TURNS
            
import random        
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.") 
    should_continue=True
    while(should_continue):   
        guess=random.randint(1,100)
        difi=int(setDificulty())
        ans=0
        while(difi!=0 and guess!=ans):
            ans=int(input("Give your guess->"))
            difi=check(guess=guess,answer=ans,turns=difi)
        str=input("Do you want to continue then press 'y' or press 'n' ->")
        if(str=='y') :
            should_continue=True
        else :
            should_continue=False
   
   
game()   
            
        
    
