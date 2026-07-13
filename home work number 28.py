try:
    n = int(input("Enter n: "))

    if n < 1:
        raise ValueError

except ValueError:
    print("Invalid input! Please enter a positive integer.")

else:
    product = 1

    for i in range(n, 0, -1):
        print(i)
        product *= i

    print("Product =", product)

finally:
    print("Program finished.")