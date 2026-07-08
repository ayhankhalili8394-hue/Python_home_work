num = 101

while num <= 999:
    if num % 2 != 0:
        
        a = num // 100
        b = (num // 10) % 10
        c = num % 10

        
        sum_digits = a + b + c

        
        if num % sum_digits == 0:
            print(num)

    num = num + 2