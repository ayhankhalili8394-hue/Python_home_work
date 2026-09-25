def find_winner():
    participants = {}

    number = int(input("How many participants? "))

    for i in range(number):
        name = input("Enter participant name: ")
        score = float(input("Enter score: "))
        participants[name] = score

    winner = min(participants, key=participants.get)

    print("Winner:", winner)
    print("Score:", participants[winner])


find_winner()
