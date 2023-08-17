import random
from Day7_Hangman_Art import stages, logo
from Day7_Hangman_WordBank import word_list

chosen_word = random.choice(word_list)
lives = 6
game_over = False
display = []
used_letters = []

# Creates a blank list that contains the number of letters for the chosen word
for _ in chosen_word:
    display += "_"
# print(chosen_word)              # Show word for debugging
print(logo)
print()
print(f"Number of lives: {lives}")
print(f"{' '.join(display)}")

# LOOP THAT KEEPS THE GAME RUNNING
while not game_over:
    guess = input("Guess a letter: ")
    # Iterates through the chosen word to determine if user guessed right
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # If user guesses wrong a life will be lost, if all lives are lost game is over
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You ran out of lives!")
    # Keep tracks of used letters
    if guess not in used_letters:
        used_letters += guess
    # If user guesses all the letters he wins and game is over
    if "_" not in display:
        game_over = True
        print("You guessed all the letters of the word!")
        print("You win!")

    # PRINTS EVERY ROUND
    print()
    print(f"{' '.join(display)}")        # Guessed letters
    print(f"Used letters: {','.join(used_letters)}")
    print(f"Number of lives {lives}")
    print(stages[lives])

print(f"The word was: {chosen_word}")
