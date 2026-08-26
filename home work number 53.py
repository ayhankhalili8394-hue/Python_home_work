def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count

print(count_vowels("Hello World"))
