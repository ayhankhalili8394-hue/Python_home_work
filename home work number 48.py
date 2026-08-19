def error_print():
    print("Error")


def twice_do():
    error_print()
    error_print()


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a < 0 and b < 0:
    twice_do()

elif a < 0 or b < 0:
    error_print()