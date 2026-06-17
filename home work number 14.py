Asking_number_of_people = eval(input("Welcome to the California! can you tell me how much people you are? "))

print(Asking_number_of_people)


if Asking_number_of_people < 1:
    print("sorry but we need more than 1 people here. ")

if Asking_number_of_people > 7:
    print("sorry but we don't have a room for 7 people. ")

Asking_number_of_nights = eval(input("Okay now can you tell me how many nights do you need to stay here? "))

print(Asking_number_of_nights)

price = Asking_number_of_nights * 10000

print(price, "dollars please.")


