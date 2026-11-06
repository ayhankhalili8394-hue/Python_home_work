import random

try:
    file = open("words.txt", "r")
    words = file.read().splitlines()
    file.close()

    if not words:
        print("The word file is empty.")

    else:
        secret_word = random.choice(words).lower()

        attempts = 5
        score = 100
        guessed_letters = []

        print("Welcome to the Word Guessing Game!")
        print("Guess the hidden word.")
        print("You have 5 attempts.")

        while attempts > 0:

            hint = ""

            for letter in secret_word:
                if letter in guessed_letters:
                    hint += letter
                else:
                    hint += "_"

            print("\nWord:", hint)

            guess = input("Enter a letter or the whole word: ").lower()

            if guess == secret_word:
                print("Congratulations! You guessed the word!")
                score += attempts * 10
                break

            elif len(guess) == 1 and guess in secret_word:
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    print("Correct letter!")
                else:
                    print("You already guessed this letter.")

            else:
                attempts -= 1
                score -= 10
                print("Wrong guess!")
                print("Attempts remaining:", attempts)

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You found the word!")
                break

        else:
            print("\nYou lost!")
            print("The correct word was:", secret_word)

        print("\nYour final score:", max(0, score))

except FileNotFoundError:
    print("The words.txt file was not found.")
