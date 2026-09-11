# Get words from the user and convert them into a list
words = input("Enter several words separated by spaces: ").split()

# Sort the list because binary search requires a sorted list
words.sort()


def binary_search(word_list, target):
    left = 0
    right = len(word_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if word_list[middle] == target:
            return True
        elif word_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


# Keep searching until the user presses Enter without entering a word
while True:
    search_word = input("Search for a word (press Enter to exit): ")

    if search_word == "":
        break

    if binary_search(words, search_word):
        print("The word is in the list.")
    else:
        print("The word is not in the list.")
