#Sunday, July 12, 2015 at 4:17 PM
import random
keepgoing = True

items = ['rock', 'paper', 'scissors']
print("Let's go, Rock, Paper, Scissors, Shoot!!")

while keepgoing:
    CPU_answer = random.choice(items)
    User = input('\nPick a random item: rock, paper, scissors:').lower()
    if CPU_answer == User:
        print('Draw!!!!!!!!')
    elif CPU_answer == 'rock' and User == 'paper':
        print('You Win!!')
    elif CPU_answer == 'scissors' and User == 'rock':
        print('You Win!!')
    elif CPU_answer == 'paper' and User == 'scissors':
        print('You Win!!')
    elif CPU_answer == 'rock' and User == 'scissors':
        print('You Lost!!')
    elif CPU_answer == 'scissors' and User == 'paper':
        print('You Lost!!')
    elif CPU_answer == 'paper' and User == 'rock':
        print('You Lost!!')
    play_again = input("\nDo you want to play again 'yes' or 'no')???").lower()
    if play_again == 'yes':
        keepgoing = True
    else:
        keepgoing = False
        
    
    



