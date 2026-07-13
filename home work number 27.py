total = 0

while True:
    try:
        number = int(input("Enter a number: "))

    except ValueError:
        print("Invalid input! Please enter an integer.")

    else:
        if number < 0:
            print("Program ended.")
            break
        elif number == 0:
            print("Sum =", total)
            total = 0
        else:
            total += number

    finally:
        print("Input checked.")