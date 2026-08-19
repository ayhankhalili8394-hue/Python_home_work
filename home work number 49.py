text = input("Enter a string: ")

new_text = ""

for x in text:
    if x < "0" or x > "9":
        new_text = new_text + x

print(new_text)