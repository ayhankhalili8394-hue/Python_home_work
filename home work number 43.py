def silver_digit(text):
    length = len(text)

    if length % 2 == 1:
        print(text[length // 2])
    else:
        print(text[length // 2 - 1], text[length // 2])

word = input("Enter a string: ")
silver_digit(word)