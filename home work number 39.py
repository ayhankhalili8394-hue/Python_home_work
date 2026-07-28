import random

while True:
    score = 0

    print("Coin Toss Game")
    print("Guess the result of the coin toss!")

    while True:
        try:
            guess = input("Enter heads or tails: ").lower()

            if guess != "heads" and guess != "tails":
                print("Please enter only 'heads' or 'tails'.")
                continue

            coin = random.choice(["heads", "tails"])
            print("Coin:", coin)

            if guess == coin:
                score += 1
                print("Correct! Score:", score)
            else:
                print("Wrong guess!")
                print("Final Score:", score)
                break

        except Exception:
            print("Invalid input.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break