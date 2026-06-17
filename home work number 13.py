num = eval(input("Enter a number: "))

if num % 2 == 0  and num % 3 == 0:
    print("it is divisible to 2 and 3")

elif num % 2 == 0:
    print("it is divisible to 2")

elif num % 3 == 0:
    print("it is divisible to 3")

else:
    print("it is not divisible to any of 2 or 3")