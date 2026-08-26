def print_even_numbers(n):
    if n < 2:
        return

    if n % 2 == 0:
        print(n)

    print_even_numbers(n - 1)

n = int(input())
print_even_numbers(n)
