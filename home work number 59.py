factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

n = int(input())
print(factorial(n))
