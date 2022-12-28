# 100 Days of Code - Udemy
# Day 4 - Rock Paper Scissors Game
# https://www.udemy.com/course/100-days-of-code/learn/lecture/18011807#overview

# Import library to generate random numbers.
import random

# ASCII art for hand gestures in rock, paper, scissors game.
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

# Lists holding choices in game.
game_text = ['Rock', 'Paper', 'Scissors']
game_images = [rock, paper, scissors]

# Ask for User's choice.
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

# Check if user's input is a valid choice.
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f'You chose: {game_text[user_choice]}')
    print(game_images[user_choice])

    # Computer randomly chooses.
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {game_text[computer_choice]}')
    print(game_images[computer_choice])

    # Logic rules for who wins in game.
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
