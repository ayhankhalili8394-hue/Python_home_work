import random

player1 = 0
player2 = 0
turn = 1

print("Snake and Ladder Game")
print("First player to reach 100 wins!\n")

while True:
    print("-" * 40)

    if turn == 1:
        input("Player 1 - Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print("Player 1 rolled:", dice)

        if player1 + dice <= 100:
            player1 += dice
        else:
            print("Player 1 must roll the exact number to reach 100.")

        if player1 == 100:
            print("\nPlayer 1 Wins!")
            break

        turn = 2

    else:
        input("Player 2 - Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print("Player 2 rolled:", dice)

        if player2 + dice <= 100:
            player2 += dice
        else:
            print("Player 2 must roll the exact number to reach 100.")

        if player2 == 100:
            print("\nPlayer 2 Wins!")
            break

        turn = 1

    print("\nCurrent Board:")
    print("Player 1 is on square", player1)
    print("Player 2 is on square", player2)