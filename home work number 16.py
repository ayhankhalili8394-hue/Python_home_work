Internet_bot = input("Hello there! press 1 to buy our limited package and press 2 to buy our unlimited package and press 3 for just our unlimited call and press 4 to buy our just unlimited internet: ")


if Internet_bot == "1":
    print("okay then")

    Asking_internet_used = eval(input("so can you tell me how much GB did you used? "))

    Asking_call_used = eval(input("so can you tell me how many minutes call time yu used? "))

    if Asking_internet_used >= 20 and Asking_call_used >= 300:
        print("I perfer you to buy our unlimited pack")

    elif Asking_internet_used >= 20 and Asking_call_used < 300:
        print("we perfer you unlimited internet pack")

    else:
        print("we perfer you unlimited call pack")


elif Internet_bot == "2":
    print("Ok done.")


elif Internet_bot == "3":
    print("Ok done.")

elif Internet_bot == "4":
    print("Ok done.")

else:
    print("invalid choice")

