import random

score = 0
current_number = random.randint(1, 9)

print("Lower / Upper Game")
print("Guess if the next number will be higher or lower.")

while True:
    print("\nCurrent number:", current_number)

    try:
        guess = input("Enter 'higher' or 'lower': ").lower()

        if guess != "higher" and guess != "lower":
            print("Please enter only 'higher' or 'lower'.")
            continue

        next_number = random.randint(1, 9)
        print("Next number:", next_number)

        if (guess == "higher" and next_number > current_number) or \
           (guess == "lower" and next_number < current_number):
            score += 1
            print("Correct!")
            current_number = next_number
        else:
            print("Wrong guess!")
            print("Your score:", score)
            break

    except Exception:
        print("Invalid input.")