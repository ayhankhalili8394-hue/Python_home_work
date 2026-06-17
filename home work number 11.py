centigrade = eval(input("Enter a centigrade please: "))

print(centigrade)

if centigrade < 1:
    print("it is ice times")

elif centigrade < 9:
    print("it is a really cold day")

elif centigrade < 16:
    print("it is quite a cold day")

elif centigrade < 23:
    print("it is a normal day")

elif centigrade < 30:
    print("it is quite a hot day")

elif centigrade > 30:
    print("it is a really hot day")


