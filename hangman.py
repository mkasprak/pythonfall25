"""
    create a "hangman" game with 8 chances to guess wrong (potential enhancement)

"""
# get random
import random

# available words
WORD_LIST= ("COFFEE", "LATTE", "MONSTER", "MATCHA")

def game(answer, display):
    print("\n" +display + "\n")
    wrong = 0
    right = 0

    guessed_letters = []

    while True:
        # display letter spots (_ _ _ _)


        # get guess from user


        # check if already guessed


        # append to guessed letters


        # Check if guess - letter in word


        # if in word redisplay and add to right (for each letter)


        # if not add to wrong


        # check if won /lost, loop or break





def main():
    """
        manage logical flow of program
    """

    my_answer = random.choice(WORD_LIST) # grab random word from list
    print(my_answer)
    my_display = "_ " * len(my_answer)

    
    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")
    game(my_answer, my_display)

main()