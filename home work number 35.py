number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if number_2 > number_1:
    while number_2 >= number_1:
        print(number_2)
        number_2 -= 1
else:
    print("The second number is not bigger than the first number.")