def find_min_max(numbers):
    result = [max(numbers), min(numbers)]
    print(result)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

find_min_max(numbers)
