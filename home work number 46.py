def count_words(text, n):
    if n <= 0:
        return False

    words = text.split()
    count = 0

    for word in words:
        if len(word) == n:
            count = count + 1

    return count


while True:
    text = input("Enter a string: ")
    n = int(input("Enter n: "))

    result = count_words(text, n)

    if result is False:
        print("Error")
    else:
        print("Number of words:", result)
        break