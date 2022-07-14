# this is the "game.py" file

print("Rock, paper, scissors, shoot!")

user_choice = input("please choose rock, paper, or scissors. ")

print("you chose " + user_choice +"!")

arr = ["rock", "paper", "scissors"]

import random

computer_choice = random.choice(arr)

print("The computer chose " + computer_choice + "!")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock beats scissors. You lose.")

print("Thank you for playing. Please play again!")