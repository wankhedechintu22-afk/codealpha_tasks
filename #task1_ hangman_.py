import random

# Predefined list of 5 words
words = ["python", "apple", "banana", "computer", "secret"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
lives = 6

print("=== Welcome to Hangman Game ===")

while lives > 0:
    # Build displayed word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    print("\nWord: " + display_word)
    print("Lives left:", lives)

    # Check for win condition
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print("\n🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        lives = lives - 1

if lives == 0:
    print("\nGame Over! The correct word was:", secret_word)