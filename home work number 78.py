import random

cards = list(range(1, 11))
random.shuffle(cards)

attempts = 3

while attempts > 0:
    print("Guess the order of the 10 cards.")
    print("Enter 10 numbers separated by spaces.")

    user_input = input("Your guess: ")
    guesses = user_input.split()

    if len(guesses) != 10:
        print("Please enter exactly 10 numbers.")
        continue

    try:
        guesses = [int(number) for number in guesses]
    except ValueError:
        print("Please enter numbers only.")
        continue

    if sorted(guesses) != list(range(1, 11)):
        print("Enter every number from 1 to 10 exactly once.")
        continue

    correct_guesses = []

    for i in range(10):
        if guesses[i] == cards[i]:
            correct_guesses.append(guesses[i])

    if guesses == cards:
        print("Congratulations! You guessed the correct order!")
        break

    attempts -= 1

    print("Correct numbers in the correct positions:", correct_guesses)
    print("Attempts remaining:", attempts)

    if attempts > 0:
        print("Try again!")

print("The correct order was:", cards)
