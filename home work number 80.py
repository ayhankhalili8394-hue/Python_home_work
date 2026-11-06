import random

roles = [
    "Mafia",
    "Doctor",
    "Detective",
    "Villager",
    "Villager",
    "Villager"
]

players = []

for i in range(len(roles)):
    name = input("Enter participant " + str(i + 1) + "'s name: ")
    players.append(name)

random.shuffle(roles)

assignments = {}

for i in range(len(roles)):
    assignments[roles[i] + "_" + str(i)] = players[i]

role_players = {}

for role in roles:
    role_players[role] = []

for key in assignments:
    role = key.rsplit("_", 1)[0]
    role_players[role].append(assignments[key])

print("\nRoles have been assigned.")

while True:
    role_name = input(
        "\nNarrator, enter a role name or 'morning is comming' to finish: "
    )

    if role_name.strip().lower() == "morning is comming":
        print("The program has ended.")
        break

    role_name = role_name.strip().title()

    if role_name in role_players:
        print("Player(s) with this role:")

        for player in role_players[role_name]:
            print(player)
    else:
        print("This role was not found.")
