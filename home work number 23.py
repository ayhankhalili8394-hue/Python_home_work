number = int(input("Enter a number: "))

sum = 0
i = 1

# Calculate the sum of cubes
while i <= number:
    sum = sum + (i ** 3)
    i = i + 1

# Print the result
print("Sum of cubes:", sum)