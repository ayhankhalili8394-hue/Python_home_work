Ask_triangle1 = eval(input("Enter a number: "))

Ask_triangle2 = eval(input("Enter a number: "))

Ask_triangle3 = eval(input("Enter a number: "))


if Ask_triangle1 == Ask_triangle2 and Ask_triangle2 == Ask_triangle3:

    print("it is a isosceles triangle")


elif Ask_triangle2 == Ask_triangle1 and Ask_triangle3 is not Ask_triangle2:

    print("It is equuilateral triangle")

else:
    print("it is not ether equuilateral triangle or isosceles triangle")


