numbers = list(map(int, input("Enter the list elements: ").split()))

while True:
    print("\n--- MENU ---")
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Sort the list")
    print("4. Count repetitions of an element")
    print("5. Find the position of an element")
    print("6. Reverse the list")
    print("7. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        value = int(input("Enter the value to add: "))
        numbers.append(value)
        print("Updated list:", numbers)

    elif choice == 2:
        value = int(input("Enter the value to remove: "))

        if value in numbers:
            numbers.remove(value)
            print("Updated list:", numbers)
        else:
            print("Value not found.")

    elif choice == 3:
        numbers.sort()
        print("Sorted list:", numbers)

    elif choice == 4:
        value = int(input("Enter the value to count: "))
        count = numbers.count(value)
        print("Number of repetitions:", count)

    elif choice == 5:
        value = int(input("Enter the value to find: "))

        if value in numbers:
            position = numbers.index(value)
            print("Position:", position)
        else:
            print("Value not found.")

    elif choice == 6:
        numbers.reverse()
        print("Reversed list:", numbers)

    elif choice == 7:
        print("Program finished.")
        break

    else:
        print("Invalid choice.")
