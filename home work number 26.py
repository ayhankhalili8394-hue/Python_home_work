count = 0
total = 0

while count < 10:
    try:
        number = int(input("Enter number {count + 1}: "))

        if number < 0:
            raise ValueError

    except ValueError:
        print("Invalid input! Please enter a non-negative number.")

    else:
        total += number
        count += 1

    finally:
        print("Input checked.")

average = total / 10
print("Average =", average)