text = input()

is_palindrome = lambda text: text == text[::-1]

print(is_palindrome(text))
