#Created August 12, 2016 at 6:13 PM
import random

option = input("Which mode do want?(C-Computer, M-Multiplayer)")
if option == 'c' or option == 'C':
    word_bank = ["Python", "Java", "Pascal", "Bash"]
    word_bank_2 = ["Variables", "Loops", "Strings", "Integers", "Floats"]

    play_again = True

    while play_again is True:
        random_word_bank = random.randint(1,2)

        if random_word_bank == 1:
            picked_word = random.choice(word_bank)
            number_of_letters = len(picked_word)
            player_name = input("Enter your name:")
            print("\n" * 100)
            print("Hello " + player_name + "!" + " Welcome to the game of Hangman!!")
            print("\n")
            print("Your word has " + str(number_of_letters) + " letters.")
            print("-" * number_of_letters)
            print("The first letter is capitalized.")
            print("Your word may have repeated letters.")
            hint = input("Need a HINT:")

            if hint == "Yes" or hint == "yes":
                print("Your word is a well-known programming language!!")

            guesses_left = number_of_letters + 1
            user_guesses = []

            while guesses_left > 0:
                print("\n")
                print("Guesses Left: " + str(guesses_left))
                entered_guess = input("Guess a letter:")
                user_guesses.append(entered_guess)


                if number_of_letters == 4:
                    for letter in picked_word:
                        if entered_guess == letter:
                            new_guess = " " + entered_guess + " \n"
                            # new_guess = "  " + entered_guess + " "+ end=""
                            if (user_guesses == 'B' and user_guesses == 'a' and user_guesses == 's' and user_guesses == 'h') or (user_guesses == 'J' and user_guesses == 'a' and user_guesses == 'v' and user_guesses == 'a'):
                                guesses_left = -1
                                print('You won!')
                                print("The word was " + picked_word)
                                answer = input("Do you want to play again?")
                                if answer == "Yes" or answer == "yes":
                                    play_again = True
                                else:
                                    print("Game is finished")
                                    play_again = False
                        else:
                            print(" - ",end="")
                            guesses_left = guesses_left - 1

                elif number_of_letters == 6:
                    for letter in picked_word:
                        if entered_guess == letter:
                            print(" " + entered_guess + " ",end="")
                            if (user_guesses == 'P' and user_guesses == 'y' and user_guesses == 't' and user_guesses == 'h' and user_guesses == 'o' and user_guesses == 'n') or (user_guesses == 'P' and user_guesses == 'a'and user_guesses == 's' and user_guesses == 'c' and user_guesses == 'a' and user_guesses == 'l'):
                                guesses_left = -1
                                print('You won')
                                print("The word was " + picked_word)
                                answer = input("Do you want to play again?")
                                if answer == "Yes" or answer == "yes":
                                    play_again = True
                                else:
                                    play_again = False
                        else:
                            print(" - ",end="")
                            guesses_left = guesses_left - 1

            if guesses_left <= 0:
                print("\n")
                print("YOU RAN OUT OF GUESSES!")
                print("The word is " + picked_word + "!")
                print("\n")
                answer = input("Do you want to play again?")
                print("\n")
                if answer == "Yes" or answer == "yes":
                    play_again = True
                else:
                    play_again = False
elif option == 'm' or option == 'M':
    pass
