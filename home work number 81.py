import random
import datetime

members = {}
books = {
    "Harry Potter": 3,
    "The Hobbit": 2,
    "1984": 1,
    "Animal Farm": 2,
    "The Little Prince": 0
}

admin_username = "admin"
admin_password = "1234"

def save_history(operation):
    file = open("library_history.txt", "a")
    file.write(operation + "\n")
    file.close()

def generate_membership():
    date = datetime.datetime.now().strftime("%Y%m%d")
    random_number = random.randint(1000, 9999)
    return str(date) + str(random_number)

def add_member():
    name = input("Enter member name: ")
    membership = generate_membership()

    while membership in members:
        membership = generate_membership()

    members[membership] = name

    print("Member added successfully!")
    print("Name:", name)
    print("Membership number:", membership)

    save_history(name + " was added as a new member.")

def delete_member():
    membership = input("Enter membership number: ")

    if membership in members:
        name = members[membership]
        del members[membership]

        print("Member deleted successfully!")
        save_history(name + " was deleted.")
    else:
        print("Member not found.")

def search_book():
    book_name = input("Enter book name: ")

    if book_name in books:
        print("Book found:", book_name)
        print("Available copies:", books[book_name])

        save_history("Searched for " + book_name)
    else:
        print("Book not found.")
        save_history("Searched for unavailable book: " + book_name)

def borrow_book(membership):
    book_name = input("Enter the book name: ")

    if book_name in books:
        if books[book_name] > 0:
            books[book_name] -= 1

            print("Book borrowed successfully!")

            save_history(
                members[membership] + " borrowed " + book_name
            )
        else:
            print("Sorry, this book is not available.")

            save_history(
                members[membership] + " tried to borrow " + book_name
            )
    else:
        print("This book does not exist.")

        save_history(
            members[membership] + " searched for " + book_name
        )

def admin_menu():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == admin_username and password == admin_password:
        while True:
            print("\nAdmin Menu")
            print("1. Add member")
            print("2. Delete member")
            print("3. Show members")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                add_member()

            elif choice == "2":
                delete_member()

            elif choice == "3":
                for membership, name in members.items():
                    print(name, ":", membership)

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    else:
        print("Incorrect username or password.")

def member_menu():
    membership = input("Enter your membership number: ")

    if membership not in members:
        print("Member not found.")
        return

    print("Welcome", members[membership])

    while True:
        print("\nMember Menu")
        print("1. Search for a book")
        print("2. Borrow a book")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_book()

        elif choice == "2":
            borrow_book(membership)

        elif choice == "3":
            break

        else:
            print("Invalid choice.")

while True:
    print("\nLibrary Management System")
    print("1. Administrator")
    print("2. Member")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        admin_menu()

    elif choice == "2":
        member_menu()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
