import random

number_of_players = int(input("Enter the number of players (2-4): "))

while number_of_players < 2 or number_of_players > 4:
    number_of_players = int(input("Enter a number between 2 and 4: "))

players = []
scores = []

for i in range(number_of_players):
    name = input("Enter player " + str(i + 1) + "'s name: ")
    players.append(name)
    scores.append(0)

for round_number in range(1, 8):
    print("\nRound", round_number)

    cards = list(range(1, 11))
    random.shuffle(cards)

    for i in range(number_of_players):
        print("\n", players[i], "'s turn", sep="")

        attempts = 3

        while attempts > 0:
            print("Guess the order of the 10 cards.")
            user_input = input("Enter 10 numbers separated by spaces: ")
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

            correct_count = 0

            for j in range(10):
                if guesses[j] == cards[j]:
                    correct_count += 1

            if guesses == cards:
                print("Perfect! You guessed the entire sequence!")
                scores[i] += 10
                break

            attempts -= 1

            print("Correct positions:", correct_count)
            print("Correct numbers:", [
                guesses[j] for j in range(10)
                if guesses[j] == cards[j]
            ])

            if attempts > 0:
                print("Attempts remaining:", attempts)

        if attempts == 0:
            scores[i] += correct_count

        print("The correct sequence was:", cards)
        print("Your total score:", scores[i])

print("\nFinal Scoreboard")

for i in range(number_of_players):
    print(players[i], ":", scores[i], "points")

highest_score = max(scores)

print("\nWinner(s):")

for i in range(number_of_players):
    if scores[i] == highest_score:
        print(players[i])

print("Highest score:", highest_score)
