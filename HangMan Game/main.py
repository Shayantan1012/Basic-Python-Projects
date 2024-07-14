from hangman_words import word_list;
from hangman_image import logo
from hangman_image import stages

print(logo)
import random
corr_word=random.choice(word_list);
display=[]

for x in range(len(corr_word)):
    display+=('_'); 
    
life=0
print(corr_word)
con=True
while(life!=len(stages)-1 and con):
    guess=input("Give the Input of a Letter->").lower()
    if(guess in corr_word):
        print(f"You've already guessed {guess}")
        for x in range (len(display)):
            if(guess==corr_word[x]):
             display[x]=guess
        print(display)
        if(not('_' in display)):
            con=False         
    else:
        life+=1
        print("You Loose your one life!!!")
        print(stages[life])
        

if(life!=len(stages)-1):
    print('Congratultes!!! You Win!!')
else:
    print("You Loose the game !!!!")                 
