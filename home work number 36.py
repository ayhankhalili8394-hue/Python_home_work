import random

number = random.randint(1, 10000)
wrong_guesses = 0

print("Number Guessing Game")
print("The computer has chosen a number between 1 and 10000.")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("The number is greater.")
            wrong_guesses += 1

        elif guess > number:
            print("The number is smaller.")
            wrong_guesses += 1

        else:
            print("Congratulations! You guessed the correct number.")
            print("Wrong guesses:", wrong_guesses)
            break

    except ValueError:
        print("Please enter a valid integer.")