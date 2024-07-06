import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    print('This is your turn ->>>>>>>\n')
    print('''Give your choice ->
      Press 0 for ROCK
      Press 1 for PAPER
      Press 2 for SCISSORS
      Press q to QUIT\n
      ''')
    
    a = input()

    if a == 'q':
        print('Game Over!')
        break

    if a == '0':
        print(rock)
    elif a == '1':
        print(paper)
    elif a == '2':
        print(scissors)
    else:
        print('Please press a correct KEY!!!!')
        continue

    x = str(random.randint(0, 2))
    print('This is Computer\'s turn ->>>>>\n')
    if x == '0':
        print(rock)
    elif x == '1':
        print(paper)
    elif x == '2':
        print(scissors)

    if a == x:
        print('No one is Qualified, try again!!!\n')
    elif a == '0':
        if x == '1':
            print('You Lose!!!')
        elif x == '2':
            print('You Won!!! 🎉🎉🎉🎉🎉')
    elif a == '1':
        if x == '0':
            print('You Won!!! 🎉🎉🎉🎉🎉')
        elif x == '2':
            print('You Lose!!!')
    elif a == '2':
        if x == '1':
            print('You Won!!! 🎉🎉🎉🎉🎉')
        elif x == '0':
            print('You Lose!!!')
