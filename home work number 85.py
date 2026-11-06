import random

try:
    file = open("words.txt", "r")
    words = file.read().splitlines()
    file.close()

    if not words:
        print("The word file is empty.")

    else:
        secret_word = random.choice(words).lower()

        letters = list(secret_word)
        random.shuffle(letters)

        scrambled_word = "".join(letters)

        while scrambled_word == secret_word and len(secret_word) > 1:
            random.shuffle(letters)
            scrambled_word = "".join(letters)

        score = 100
        attempts = 3

        print("Welcome to the Scrambled Word Game!")
        print("Unscramble this word:", scrambled_word)

        while attempts > 0:
            guess = input("Enter your guess: ").lower()

            if guess == secret_word:
                print("Congratulations! Your answer is correct!")
                score += attempts * 10
                break

            else:
                attempts -= 1
                score -= 20

                print("Wrong answer!")
                print("Attempts remaining:", attempts)

        if attempts == 0:
            print("You lost!")
            print("The correct word was:", secret_word)

        print("Your final score:", max(0, score))

except FileNotFoundError:
    print("The words.txt file was not found.")
