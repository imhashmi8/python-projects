# Display Art
from signal import valid_signals

from art import logo,vs
from game_data import data
import random
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Function to display account details
def format_data(account):
    """Format the account data and return in printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"

# Function to check if user guess is correct and return if they got it right
def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Make the game repeatable

while game_should_continue:
# Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")


    # Ask the user for a guess
    guess= input("Who has more followers? Type 'A' or 'B' : ").lower()

    # Clear the screen
    print("\n" * 50)
    print(logo)

    # Check if user is correct
    # Get follower count of each count
    # Use if statement to check if the user is correct
    a_account_count = account_a["follower_count"]
    b_account_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_account_count,b_account_count)

    # Give user feedback on their guess

    if is_correct:
        score +=1
        print(f"You're right! Current Score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Your final score is {score}")
