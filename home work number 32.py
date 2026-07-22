while True:
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if len(string1) > len(string2):
        print(string1)
    elif len(string2) > len(string1):
        print(string2)
    else:
        print("Both strings have the same length.")

    break
