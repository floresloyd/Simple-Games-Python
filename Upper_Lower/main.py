import random
from game_data import data
from art import logo, vs


def format_data(account):
    # Formats data
    account_name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{account_name}, {description}, from {country}."


def check_answer(choice, a_followers, b_followers):
    """ Takes user's selection and checks if it is right"""
    # if a > b our conditional check if user selected "a" and returns T/F
    # else a < b checks if user selected "b" since b is greater
    if a_followers > b_followers:
        return choice == "a"
    else:
        return choice == "b"


def upper_lower():
    score = 0
    game_should_continue = True
    option_b = random.choice(data)      # Selects a new account

    while game_should_continue:
        option_a = option_b             # Generated from initial run or the previous option B
        option_b = random.choice(data)  # Generates a new account
        if option_a == option_b:        # Re-generates if they match
            option_b = random.choice(data)
        follower_count_a = option_a["follower_count"]
        follower_count_b = option_b["follower_count"]
        print(logo)
        print(f"Compare A: {format_data(option_a)} ")
        print(vs)
        print(f"Compare B: {format_data(option_b)}")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(user_input, follower_count_a, follower_count_b)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"You're wrong! Final score: {score} ")


upper_lower()