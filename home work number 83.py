file_name = input("Enter the first file name: ")

try:
    file = open(file_name, "r", encoding="utf-8")
    text = file.read()
    file.close()

    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    sorted_frequency = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    output_file = open("results.txt", "w", encoding="utf-8")

    for character, count in sorted_frequency:
        if character == "\n":
            character = "New Line"
        elif character == " ":
            character = "Space"

        output_file.write(character + " : " + str(count) + "\n")

    output_file.close()

    print("Character frequencies saved successfully in results.txt")

except FileNotFoundError:
    print("File not found.")
