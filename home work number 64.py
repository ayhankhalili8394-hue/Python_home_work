odd_numbers = lambda a, b: [x for x in range(a, b + 1) if x % 2 != 0]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = odd_numbers(num1, num2)

print(result)
