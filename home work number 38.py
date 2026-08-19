import random

def print_board(player1, player2):
    for row in range(10, 0, -1):
        for col in range(1, 11):
            number = (row - 1) * 10 + col

            if number == player1:
                print(" A ", end="")
            elif number == player2:
                print(" B ", end="")
            else:
                print(f"{number:3}", end="")

            print("|", end="")

        print()
        print("-" * 40)


player1 = 0
player2 = 0

while True:

    print_board(player1, player2)

    input("Player A - Press Enter to roll the dice...")
    dice = random.randint(1, 6)

    print("Player A rolled:", dice)

    if player1 + dice <= 100:
        player1 = player1 + dice
    else:
        print("Too far! Player A stays in the same place.")

    if player1 == 100:
        print_board(player1, player2)
        print("Player A wins!")
        break

    print_board(player1, player2)

    input("Player B - Press Enter to roll the dice...")
    dice = random.randint(1, 6)

    print("Player B rolled:", dice)

    if player2 + dice <= 100:
        player2 = player2 + dice
    else:
        print("Too far! Player B stays in the same place.")

    if player2 == 100:
        print_board(player1, player2)
        print("Player B wins!")
        break