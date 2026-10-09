
import random
import os

PLAYER_COUNT = 15

ROLE_LIST = (
    ["Werewolf"] * 4
    + ["Villager"] * 7
    + ["Seer", "Doctor"]
    + ["Hunter"] * 2
)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="Press Enter to continue..."):
    input(message)


def living_players(players):
    return [player for player in players if player["alive"]]


def find_player(players, name):
    for player in players:
        if player["name"].lower() == name.lower():
            return player
    return None


def choose_player(players, candidates, prompt, excluded=None):
    excluded = excluded or []
    choices = [
        player for player in candidates
        if player["alive"] and player["name"] not in excluded
    ]

    if not choices:
        return None

    while True:
        clear_screen()
        print(prompt)
        print()

        for index, player in enumerate(choices, 1):
            print(str(index) + ". " + player["name"])

        answer = input("\nEnter a player number: ").strip()

        if answer.isdigit():
            number = int(answer)

            if 1 <= number <= len(choices):
                return choices[number - 1]

        print("Please enter a valid number.")
        pause()


def reveal_roles(players):
    for player in players:
        clear_screen()
        print("Pass the computer to " + player["name"] + ".")
        pause("When you are ready, press Enter...")

        clear_screen()
        print("Your name: " + player["name"])
        print("Your secret role: " + player["role"])

        if player["role"] == "Werewolf":
            teammates = [
                other["name"] for other in players
                if other["role"] == "Werewolf"
                and other is not player
            ]

            print("\nYour Werewolf teammates are:")

            for name in teammates:
                print("- " + name)

            print("\nChoose victims with your team at night.")

        elif player["role"] == "Villager":
            print("\nYou are on the Village team.")
            print("Find the Werewolves and vote them out.")

        elif player["role"] == "Seer":
            print("\nYou are on the Village team.")
            print("You can investigate a player each night.")

        elif player["role"] == "Doctor":
            print("\nYou are on the Village team.")
            print("You can protect a player each night.")
            print("You cannot protect the same player on")
            print("two consecutive nights.")

        elif player["role"] == "Hunter":
            print("\nYou are on the Village team.")
            print("When eliminated, you can eliminate")
            print("one living player with you.")

        pause("\nMemorize your role. Press Enter to hide it.")

    clear_screen()
    print("Everyone has received their secret role.")
    pause()


def get_werewolf_target(players):
    wolves = [
        player for player in players
        if player["alive"] and player["role"] == "Werewolf"
    ]

    candidates = [
        player for player in players
        if player["alive"] and player["role"] != "Werewolf"
    ]

    if not wolves or not candidates:
        return None

    votes = {}

    for wolf in wolves:
        clear_screen()
        print("WEREWOLF NIGHT TURN")
        print("Pass the computer to " + wolf["name"] + ".")
        pause("Press Enter when ready...")

        target = choose_player(
            players,
            candidates,
            "Choose a player to attack."
        )

        if target:
            votes[target["name"]] = (
                votes.get(target["name"], 0) + 1
            )

        clear_screen()
        print("Your choice has been recorded.")
        pause("Pass the computer to the next Werewolf.")

    highest = max(votes.values())

    tied_names = [
        name for name, count in votes.items()
        if count == highest
    ]

    chosen_name = random.choice(tied_names)

    return find_player(players, chosen_name)


def get_doctor_target(players, last_protected_name):
    doctors = [
        player for player in players
        if player["alive"] and player["role"] == "Doctor"
    ]

    if not doctors:
        return None

    doctor = doctors[0]

    candidates = [
        player for player in players
        if player["alive"]
        and player["name"] != last_protected_name
    ]

    if not candidates:
        return None

    clear_screen()
    print("DOCTOR NIGHT TURN")
    print("Pass the computer to " + doctor["name"] + ".")
    pause("Press Enter when ready...")

    target = choose_player(
        players,
        candidates,
        "Choose someone to protect tonight."
    )

    clear_screen()
    print("Your protection choice has been recorded.")
    pause("Pass the computer on.")

    return target


