
players = int(input("Enter the number of players (2 to 4): "))

while players < 2 or players > 4:
    players = int(input("Please enter a number between 2 and 4: "))

scores = {}

for i in range(players):
    name = input("Enter player name: ")
    scores[name] = 0

for round_number in range(1, 8):
    print("Round", round_number)

    for name in scores:
        points = int(input(name + ", enter your points: "))
        scores[name] += points

print("Final Scoreboard:")

for name, score in scores.items():
    print(name, ":", score)

winner = max(scores, key=scores.get)

print("The winner is:", winner)
print("Final score:", scores[winner])