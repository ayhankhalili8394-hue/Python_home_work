phone_book = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    phone_book[name] = phone
    print("Contact added successfully.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_phone_by_name():
    name = input("Enter name: ")

    if name in phone_book:
        print("Phone number:", phone_book[name])
    else:
        print("Contact not found.")


def search_name_by_phone():
    phone = input("Enter phone number: ")

    for name, number in phone_book.items():
        if number == phone:
            print("Name:", name)
            return

    print("Phone number not found.")


def change_phone():
    name = input("Enter name: ")

    if name in phone_book:
        new_phone = input("Enter new phone number: ")
        phone_book[name] = new_phone
        print("Phone number changed successfully.")
    else:
        print("Contact not found.")


def change_name():
    old_name = input("Enter current name: ")

    if old_name in phone_book:
        new_name = input("Enter new name: ")
        phone = phone_book[old_name]

        del phone_book[old_name]
        phone_book[new_name] = phone

        print("Name changed successfully.")
    else:
        print("Contact not found.")


def show_phone_book():
    if len(phone_book) == 0:
        print("Phone book is empty.")
    else:
        print("\n--- PHONE BOOK ---")

        for name, phone in phone_book.items():
            print("Name:", name, "| Phone:", phone)


while True:
    print("\n--- PHONE BOOK MENU ---")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Search phone by name")
    print("4. Search name by phone")
    print("5. Change phone number")
    print("6. Change name")
    print("7. Show phone book")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        delete_contact()

    elif choice == "3":
        search_phone_by_name()

    elif choice == "4":
        search_name_by_phone()

    elif choice == "5":
        change_phone()

    elif choice == "6":
        change_name()

    elif choice == "7":
        show_phone_book()

    elif choice == "8":
        print("Program finished.")
        break

    else:
        print("Invalid choice.")
