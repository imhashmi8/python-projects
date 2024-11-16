import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

# Prints the actual word. Uncomment to show
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f'You have already guessed "{guess}"')

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print("***********************YOU LOSE**********************")
            print(f"Correct word was '{chosen_word}'q")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(hangman_art.stages[lives])

