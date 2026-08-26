text = "Hello World"

count_consonants = lambda text: sum(
    1 for letter in text.lower()
    if letter.isalpha() and letter not in "aeiou"
)

print(count_consonants(text))
