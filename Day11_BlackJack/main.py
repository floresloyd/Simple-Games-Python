import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
my_score = 0
computer_cards = []
computer_score = 0
game_over = False


while not game_over:
    if my_score == 0:
        # User's Cards
        my_cards.append(cards[random.randint(0, 12)])
        my_cards.append(cards[random.randint(0, 12)])
        for x in my_cards:
            my_score += x
        # Computer's Cards
        computer_cards.append(cards[random.randint(0, 12)])
        computer_cards.append(cards[random.randint(0, 12)])
        for x in computer_cards:
            computer_score += x

        print(f"Your cards are: {my_cards}, with a total score of: {my_score}")
        print(f"Computer's first card: {computer_cards[0]} score: {computer_score}")
        print()
    else:
        while not game_over:
            if input("Do you want to draw another card? 'y' or 'n'? : ") == 'y':
                my_cards.append(cards[random.randint(0, 12)])
                computer_cards.append(cards[random.randint(0, 12)])
                my_score += my_cards[len(my_cards) - 1]
                computer_score += computer_cards[len(computer_cards) - 1]
                print(f"Your cards are: {my_cards}, with a total score of: {my_score}")
                print()

                if my_score >= 22:
                    print(f"You loose! Final score : {my_score}")
                    game_over = True

            else:
                print(f"Your cards are: {my_cards}, with a total score of: {my_score}")
                game_over = True

                if my_score > computer_score:
                    print("You win!")
                if computer_score > my_score:
                    print("Computer wins!")
                if my_score == computer_score:
                    print("Draw!")
                if computer_score > 21:
                    print("You win, computer scored over 21")
print(f"Your final score: {my_score} | Computer final score: {computer_score}")