try:
    number = int(input("Enter a number: "))

    if number < 0:
        number = -number

except ValueError:
    print("Invalid input! Please enter an integer.")

else:
    smallest = 9

    while number > 0:
        digit = number % 10

        if digit < smallest:
            smallest = digit

        number //= 10

    print("Smallest digit =", smallest)

finally:
    print("Program finished.")