
correct_numbers = [3, 7, 2, 9, 5]
correct_guesses = []
attempts = 3

while attempts > 0:
    print("Enter your guesses separated by spaces.")
    user_input = input("Your guesses: ")
    guesses = list(map(int, user_input.split()))

    for number in guesses:
        if number in correct_numbers and number not in correct_guesses:
            correct_guesses.append(number)

    if guesses == correct_numbers:
        print("Congratulations! You guessed the correct sequence!")
        break

    attempts -= 1
    print("Correct guesses:", correct_guesses)
    print("Attempts remaining:", attempts)

print("Correct sequence:", correct_numbers)