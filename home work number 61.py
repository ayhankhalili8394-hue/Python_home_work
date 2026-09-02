def hop_game(number):
    for i in range(number, number + 15):
        if i % 3 == 0 or "3" in str(i):
            print("Hop")
        else:
            print(i)


number = int(input("Enter a number: "))
hop_game(number)
