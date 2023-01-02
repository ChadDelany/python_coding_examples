# 100 Days of Code - Udemy
# Day 7 - Hangman Game
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19140848#overview

# import random to be able to randomly chose a word
import random
# Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
# Import the logo and stages from hangman_art.py
from hangman_art import logo, stages
# clear function for Linux
import os
clear = lambda: os.system('clear')

# Randomly chose the word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initial Variables declared
end_of_game = False
lives = 6

# Print the logo to start the game
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# print(stages[-1])

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Clear screen to discard verbose previous input.
    clear()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # If guess is correct, replace "_" with letter in display.
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print current stage of hangman
    print(stages[(lives)])