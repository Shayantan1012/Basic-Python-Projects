from art import logo,vs
print(logo)

from game_data import data
import random
def play_game():
    should_continue=True
    while(should_continue):
        score=0;
        while(True):  
                a=random.choice(data)
                print(a)
                b=random.choice(data)
                while(a==b):
                    b=random.choice(data)
                #For First question///
                print(f"A.{a['name']}, a {a['description']}, from {a['country']}")
                
                print(vs)
            
                print(f"B.{b['name']}, a {b['description']}, from {b['country']}")
                folloA=a['follower_count']
                folloB=b['follower_count']
                ans=(input('Whose followers is greater????->').upper())
                
                if(ans=='A' and folloA<folloB):
                    print('You Loose!!☕!')
                    break;
                elif(ans=='A' and folloA>folloB):
                    print('You Win!!!')   
                    score+=1 
                elif(ans=='B' and folloA<folloB):
                    print('You Win!!!')
                    score+=1 

                elif(ans=='B' and folloA>folloB):
                    print('You Loose!!!☕')  
                    break;  
                
            
        print(f'Your Score is->{score}')
        char=input("Do you want to continue then give 'Y' Or 'N'->").lower()
        print("Women☕")
        if(char=='y'):
            should_continue=True    
        else:
            should_continue=False    

play_game()

