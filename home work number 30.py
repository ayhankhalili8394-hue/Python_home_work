try:
    num = int(input("Enter an integer: "))

except ValueError:
    print("Invalid input! Please enter an integer.")

else:
    reverse = 0
    n = abs(num)

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if num < 0:
        reverse = -reverse

    print("Reverse =", reverse)

finally:
    print("Program finished.")