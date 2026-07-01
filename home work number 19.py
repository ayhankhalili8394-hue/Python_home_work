# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest and smallest numbers
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

# Display the results
print("Largest number:", largest)
print("Smallest number:", smallest)