#Created August 12, 2016 at 2:27 PM
import random
print("Guess a number from 1-5")
hello = 6
play_again = True
while play_again is True:
    picked_number = random.randrange(1, 5)
    while hello > 5:
        guess = input("What is your guess?")
        guess = guess.rstrip()
        if int(guess) == picked_number:
            print("Congratulations!!That is......................... correct!!")
            answer = input("Do you want to play again?(Yes/No)")
            answer = answer.rstrip()
            if answer == "Yes":
                play_again = True
                picked_number = random.randrange(1, 5)
            else:
                play_again = False
                hello = 4
        elif int(guess) != picked_number:
            print("Congratulations.That is................ incorrect! Keep trying!")
            hello = 6
print("Game is finshed!!!!!!!")



