def numbers(a, b, c, d):
    if a == b or a == c or a == d or b == c or b == d or c == d:
        print("Error")
        return

    digits = [a, b, c, d]
    result = []

    for i in digits:
        for j in digits:
            for k in digits:
                for l in digits:
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        number = i * 1000 + j * 100 + k * 10 + l
                        result.append(number)

    result.sort(reverse=True)

    for x in result:
        print(x)


numbers(1, 2, 3, 4)