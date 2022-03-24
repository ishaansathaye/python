#Created August 13, 2016 at 11:36 AM
import random

option = input("Which mode do want?(Computer, Multiplayer)")
if option == 'c' or option == 'C' or option == 'computer' or option == 'Computer':
    word_bank = ["Python", "Java", "Pascal", "Bash"]

    play_again = True

    while play_again is True:
        picked_word = random.choice(word_bank)
        number_of_letters = len(picked_word)
        player_name = input("Enter your name:")
        print("\n" * 100)
        print("Hello " + player_name + "!" + " Welcome to the game of Hangman!!")
        print("\n")
        print("Your word has " + str(number_of_letters) + " letters.")
        print(" - " * number_of_letters)
        print("Your word may have repeated letters.")
        hint = input("Need a HINT:")

        if hint == "Yes" or hint == "yes" or hint == "y":
            print("Your word is a well-known programming language!!")

        guesses_left = number_of_letters + 1
        user_guesses = []
        True_List = [False] * number_of_letters

        while guesses_left > 0:
            print("\n")
            print("Guesses Left: " + str(guesses_left))
            entered_guess = input("Guess a letter:")
            user_guesses.append(entered_guess)
            correct_guess = False
            j = 0
            correct = False
            for letter in picked_word:
                if entered_guess.lower() == letter.lower():
                    True_List[j] = True
                    correct = True
                j += 1
            i = 0
            for B in True_List:
                if B == True:
                    print(" " + picked_word[i] + " ",end="")
                else:
                    print(" - ",end="")
                i += 1
            print()
            if correct:
                print("CORRECT")
                correct_guess = True
            else:
                print("Incorrect")
            if not correct_guess:
                guesses_left -= 1
            if (True_List == [True] * number_of_letters) and (guesses_left >= 0):
                guesses_left = -1
                print("\nYOU WON!!!!!")
                print("The word was " + picked_word + '.')
                answer = input("\nDo you want to play again?")
                print("\n")
                if answer == "Yes" or answer == "yes" or answer == 'y':
                    play_again = True
                else:
                    print("Game Over")
                    play_again = False


        if (guesses_left <= 0) and (True_List != [True] * number_of_letters):
            print("\n")
            print("YOU RAN OUT OF GUESSES!")
            print("The word is " + picked_word + "!")
            print("\n")
            answer = input("\nDo you want to play again?")
            print("\n")
            if answer == "Yes" or answer == "yes" or answer == 'y':
                play_again = True
            else:
                print("Game Over")
                play_again = False

elif option == 'm' or option == 'M' or option == 'multiplayer' or option == 'Multiplayer':
    play_again = True

    while play_again is True:
        print("\nGame Master: The user who enters the word.")
        game_master = input("Game Master! Enter your name:")
        print(game_master + "!" + " You have been chosen to enter a word.")
        guesser = input("\nGuesser! Enter your name:")
        print(guesser + "!" + " You have been chosen to guess the word Game Master has entered.")
        print("\nREMEMBER " + guesser.upper() + " YOU CAN NOT LOOK WHILE " + game_master.upper() + " IS TYPING.")
        picked_word = input("\nGame Master enter your word:")
        entered_hint = input("Game Master enter a hint for the guesser:")

        number_of_letters = len(picked_word)
        print("\n" * 100)
        print("Hello " + guesser + "!" + " Welcome to the game of Hangman!!")
        print("\n")
        print("Game Master's word has " + str(number_of_letters) + " letters.")
        print(" - " * number_of_letters)
        print("Your word may have repeated letters.")
        hint = input("Need a HINT:")

        if hint == "Yes" or hint == "yes" or hint == 'y':
            print(entered_hint)

        guesses_left = number_of_letters + 1
        user_guesses = []
        True_List = [False] * number_of_letters

        while guesses_left > 0:
            print("\n")
            print("Guesses Left: " + str(guesses_left))
            entered_guess = input("Guess a letter:")
            user_guesses.append(entered_guess)
            correct_guess = False
            j = 0
            correct = False
            for letter in picked_word:
                if entered_guess.lower() == letter.lower():
                    True_List[j] = True
                    correct = True
                j += 1
            i = 0
            for B in True_List:
                if B == True:
                    print(" " + picked_word[i] + " ",end="")
                else:
                    print(" - ",end="")
                i += 1
            print()
            if correct:
                print("CORRECT")
                correct_guess = True
            else:
                print("Incorrect")

            if not correct_guess:
                guesses_left -= 1
            if (True_List == [True] * number_of_letters) and (guesses_left >= 0):
                guesses_left = -1
                print("\nYOU WON!!!!!")
                print("The word was " + picked_word + '.')
                answer = input("\nDo you want to play again?")
                print("\n")
                if answer == "Yes" or answer == "yes" or answer == 'y':
                    play_again = True
                else:
                    print("Game Over")
                    play_again = False

        if (guesses_left <= 0) and (True_List != [True] * number_of_letters):
            print("\n")
            print("YOU RAN OUT OF GUESSES!")
            print("The word is " + picked_word + "!")
            print("\n")
            answer = input("\nDo you want to play again?")
            print("\n")
            if answer == "Yes" or answer == "yes" or answer == 'y':
                play_again = True
            else:
                print("Game Over")
                play_again = False


