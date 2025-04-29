from random import randint

import art

# lives based on level
easy_level_life = 10
hard_level_life = 5

# Function to check user guess against actual answer and decrease the number of attempts
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it right! The answer is {actual_answer}")

def game():
    print(art.logo)
    # Print the welcome messages
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    # Choosing a random number between 1-100
    answer= randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        # Exit the game if no turn left
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess Again")


#Function to set user difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return easy_level_life
    else:
        return hard_level_life

# Calling the difficulty function and let the user guess a number

game()
