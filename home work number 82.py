file_name = input("Enter the file name: ")

try:
    file = open(file_name, "r", encoding="utf-8")

    text = file.read()

    file.close()

    lines = text.splitlines()
    words = text.split()
    characters = len(text)

    print("\nFile Analysis Results")
    print("----------------------")

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", characters)

except FileNotFoundError:
    print("File not found.")

