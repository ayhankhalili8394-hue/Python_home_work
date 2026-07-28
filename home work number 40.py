import random

print("Dice Betting Game")

while True:
    try:
        prediction = int(input("How many points do you think you will score? "))

        if prediction < 0:
            print("Please enter a positive number.")
            continue
        break

    except ValueError:
        print("Please enter a valid integer.")

total = 0

print("\nRolling the dice 5 times...\n")

for i in range(1, 6):
    dice = random.randint(1, 6)
    print("Roll", i, ":", dice)

    total += dice

    if dice == 6:
        print("Bonus! You rolled a 6!")

print("\nTotal points:", total)

if total < prediction:
    final_score = 0
    print("You did not reach your prediction.")
elif total == prediction:
    final_score = prediction
    print("You reached your prediction!")
else:
    final_score = prediction * 5 + (total - prediction)
    print("You exceeded your prediction!")

print("Final Score:", final_score)