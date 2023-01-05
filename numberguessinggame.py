import random
import sys

# Greet and Start
user_input = input("Want to play the number guessing game: Y/N ? : ").lower()
if user_input == "n":
    sys.exit()
elif user_input != "y":
    print("Error, only type n or y")
    sys.exit()


# Gameplay
def play_game():
    useless_variable = ""
    answer = random.randint(0, 25)

    user_guess = int(input("I'm thinking of a number between 0 and 25, What is it? : "))

    if user_guess == answer:
        print("You Win!")
    elif user_guess != answer:
        print("Try Again!")
    elif user_guess == str(answer):
        print("Use only numbers!!")

# Main Game Loop
guesses = 0
while guesses < 3:
    play_game()
    guesses += 1
