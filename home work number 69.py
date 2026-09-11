# Get the encrypted map instructions from the user
encrypted = tuple(input("Enter the map instructions: ").split())

# Reverse the tuple to get the correct instructions
correct_instructions = encrypted[::-1]

# Display the correct map instructions
print("Correct map instructions:")

for word in correct_instructions:
    print(word, end=" ")
