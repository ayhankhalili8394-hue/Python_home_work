import random

try:
    file = open("words.txt", "r")
    words = file.read().splitlines()
    file.close()

    if not words:
        print("The word file is empty.")

    else:
        secret_word = random.choice(words).lower()

        guessed_letters = []
        attempts = 6
        score = 100

        print("Welcome to Hangman!")
        print("Guess the hidden word one letter at a time.")

        while attempts > 0:

            display_word = ""

            for letter in secret_word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "

            print("\nWord:", display_word)
            print("Attempts remaining:", attempts)
            print("Guessed letters:", guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You won!")
                score += attempts * 10
                break

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter one letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed this letter.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct guess!")
            else:
                print("Wrong guess!")
                attempts -= 1
                score -= 10

        else:
            print("\nGame over!")
            print("The correct word was:", secret_word)

        print("\nYour final score:", max(0, score))

except FileNotFoundError:
    print("The words.txt file was not found.")
