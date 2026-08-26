def multiply_nonzero_digits(n):
    if n == 0:
        return 1

    digit = n % 10

    if digit == 0:
        return multiply_nonzero_digits(n // 10)

    return digit * multiply_nonzero_digits(n // 10)

n = int(input())
print(multiply_nonzero_digits(n))
