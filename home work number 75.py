
roles = {
    "villager": "Ayhan",
    "doctor": "Ali",
    "detective": "Sara",
    "mafia": "Reza"
}

while True:
    role = input("Narrator, enter a role name: ")

    if role == "morning":
        print("The program has ended.")
        break

    if role in roles:
        print("Player:", roles[role])
        print("Role:", role)
    else:
        print("This role was not found.")
