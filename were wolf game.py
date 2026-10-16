import random


def hide_screen():
    print("\n" * 25)


def choose_from_list(prompt, options):
    if not options:
        return None

    while True:
        print()

        for number, option in enumerate(options, 1):
            print(str(number) + ". " + option)

        choice = input(prompt).strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(options):
                return options[number - 1]

        for option in options:
            if choice.lower() == option.lower():
                return option

        print("Please choose a listed name or number.")


def make_player_names():
    name_pool = [
        "Aiden", "Alex", "Amber", "Aria", "Ash", "Avery",
        "Blake", "Brooke", "Cameron", "Casey", "Charlie",
        "Chloe", "Chris", "Dakota", "Daniel", "Eden",
        "Elliot", "Emma", "Evan", "Felix", "Finn", "Harper",
        "Hazel", "Iris", "Jack", "Jade", "Jamie", "Jordan",
        "Kai", "Leo", "Lily", "Logan", "Luna", "Maya",
        "Mia", "Morgan", "Noah", "Nora", "Oliver", "Parker",
        "Quinn", "Riley", "Rowan", "Sam", "Sofia", "Taylor",
        "Theo", "Violet", "Willow", "Zoe"
    ]

    return random.sample(name_pool, 15)


def choose_player_name():
    players = make_player_names()

    print("WEREWOLF: YOU VS 14 ROBOTS")
    print()
    print("The computer randomly generated these 15 names:\n")

    for name in players:
        print(name)

    print()
    print("Choose ONE name for yourself.")
    print("The other 14 names will belong to robots.")

    user_name = choose_from_list(
        "Choose your player name: ",
        players
    )

    print()
    print("You are playing as " + user_name + ".")
    print("The other 14 players are computer-controlled robots.")

    input("Press Enter to assign the secret roles.")

    return players, user_name


def assign_roles(players):
    role_list = (
        ["Werewolf"] * 4
        + ["Villager"] * 7
        + ["Seer"]
        + ["Doctor"]
        + ["Hunter"] * 2
    )

    random.shuffle(role_list)

    roles = {}

    for number in range(len(players)):
        roles[players[number]] = role_list[number]

    return roles


def reveal_user_role(user_name, roles, players):
    hide_screen()

    print("YOUR SECRET ROLE")
    print()
    print("Your name: " + user_name)
    print("Your role: " + roles[user_name])
    print()

    if roles[user_name] == "Werewolf":
        teammates = [
            player for player in players
            if roles[player] == "Werewolf"
            and player != user_name
        ]

        print("Your Werewolf teammates are:")
        print(", ".join(teammates))
        print()
        print("At night, choose someone to attack.")

    elif roles[user_name] == "Villager":
        print("You are a Villager.")
        print("Find and vote out the Werewolves.")

    elif roles[user_name] == "Seer":
        print("You are the Seer.")
        print("Investigate one living player each night.")

    elif roles[user_name] == "Doctor":
        print("You are the Doctor.")
        print("Protect one living player each night.")
        print("You cannot protect the same person")
        print("two nights in a row.")

    elif roles[user_name] == "Hunter":
        print("You are the Hunter.")
        print("When eliminated, you may eliminate")
        print("one living player with you.")

    input("\nMemorize your role. Press Enter to start the game.")

    hide_screen()


def check_winner(alive, roles):
    wolf_count = sum(
        1 for player in alive
        if roles[player] == "Werewolf"
    )

    other_count = len(alive) - wolf_count

    if wolf_count == 0:
        return "Village"

    if wolf_count >= other_count:
        return "Werewolves"

    return None


def eliminate_player(name, alive, roles, user_name, reason):
    queue = [(name, reason)]

    while queue:
        victim, why = queue.pop(0)

        if victim not in alive:
            continue

        alive.remove(victim)

        print()
        print(victim + " was eliminated because of " + why + ".")
        print(victim + "'s role was " + roles[victim] + ".")

        if roles[victim] == "Hunter" and alive:
            print()
            print(victim + " was the Hunter and gets a final shot!")

            if victim == user_name:
                target = choose_from_list(
                    "Choose a living player to eliminate: ",
                    alive.copy()
                )

            else:
                target = random.choice(alive)
                print("The robot Hunter chose " + target + ".")

            if target is not None:
                queue.append(
                    (target, "the Hunter's final shot")
                )


def bot_vote(voter, choices, roles, suspicions):
    if not choices:
        return None

    if roles[voter] == "Werewolf":
        non_wolves = [
            target for target in choices
            if roles[target] != "Werewolf"
        ]

        if non_wolves:
            return random.choice(non_wolves)

        return random.choice(choices)

    highest_suspicion = max(
        suspicions[target] for target in choices
    )

    if highest_suspicion > 0:
        suspicious_players = [
            target for target in choices
            if suspicions[target] == highest_suspicion
        ]

        return random.choice(suspicious_players)

    return random.choice(choices)


def night_phase(alive, roles, user_name, last_protected, suspicions):
    print("NIGHT")
    print()
    print("The robots perform their actions automatically.")

    input("Press Enter to continue.")

    hide_screen()

    living_wolves = [
        player for player in alive
        if roles[player] == "Werewolf"
    ]

    possible_targets = [
        player for player in alive
        if roles[player] != "Werewolf"
    ]

    wolf_votes = []

    for wolf in living_wolves:

        if wolf == user_name:
            print("You are a Werewolf.")
            print("Choose someone to attack tonight.")

            target = choose_from_list(
                "Choose your target: ",
                possible_targets
            )

        else:
            target = random.choice(possible_targets)

        if target is not None:
            wolf_votes.append(target)

    wolf_target = None

    if wolf_votes:
        vote_counts = {}

        for target in wolf_votes:
            vote_counts[target] = vote_counts.get(target, 0) + 1

        highest = max(vote_counts.values())

        leaders = [
            target for target in vote_counts
            if vote_counts[target] == highest
        ]

        wolf_target = random.choice(leaders)

        if len(leaders) > 1:
            print("The Werewolves tied their votes.")
            print("A tied target was chosen randomly.")

    protected = None

    doctors = [
        player for player in alive
        if roles[player] == "Doctor"
    ]

    if doctors:
        doctor = doctors[0]

        doctor_choices = [
            player for player in alive
            if player != last_protected
        ]

        if doctor_choices:

            if doctor == user_name:
                print()
                print("You are the Doctor.")
                print("Choose someone to protect.")

                protected = choose_from_list(
                    "Protect: ",
                    doctor_choices
                )

            else:
                protected = random.choice(doctor_choices)

            last_protected = protected

    seers = [
        player for player in alive
        if roles[player] == "Seer"
    ]

    if seers:
        seer = seers[0]

        seer_choices = [
            player for player in alive
            if player != seer
        ]

        if seer_choices:

            if seer == user_name:
                print()
                print("You are the Seer.")
                print("Choose someone to investigate.")

                checked = choose_from_list(
                    "Investigate: ",
                    seer_choices
                )

                if roles[checked] == "Werewolf":
                    print(checked + " IS a Werewolf!")
                    suspicions[checked] += 4

                else:
                    print(checked + " is NOT a Werewolf.")

                input("Memorize the result. Press Enter to continue.")

                hide_screen()

            else:
                checked = random.choice(seer_choices)

                if roles[checked] == "Werewolf":
                    suspicions[checked] += 4

    if wolf_target is None:
        print("Nobody was attacked tonight.")

    elif wolf_target == protected:
        print("Morning arrives!")
        print("The Doctor saved the target.")
        print("Nobody was eliminated by the attack.")

    else:
        print("Morning arrives!")
        print("Someone was attacked during the night.")

        eliminate_player(
            wolf_target,
            alive,
            roles,
            user_name,
            "the Werewolves' attack"
        )

    input("\nPress Enter to continue to the day.")

    hide_screen()

    return last_protected


def collect_votes(alive, allowed_targets, roles, user_name, suspicions):
    vote_counts = {}

    for voter in alive.copy():

        choices = [
            target for target in allowed_targets
            if target != voter
        ]

        if not choices:
            continue

        if voter == user_name:
            print("DAYTIME VOTING")
            print("Choose who you think is a Werewolf.")

            vote = choose_from_list(
                "Your vote: ",
                choices
            )

        else:
            vote = bot_vote(
                voter,
                choices,
                roles,
                suspicions
            )

        if vote is not None:
            vote_counts[vote] = vote_counts.get(vote, 0) + 1

    return vote_counts


def top_voters(vote_counts):
    if not vote_counts:
        return []

    highest = max(vote_counts.values())

    return [
        player for player, votes in vote_counts.items()
        if votes == highest
    ]


def show_vote_results(alive, vote_counts):
    print("\nVOTING RESULTS")

    for player in alive:
        print(
            player + ": "
            + str(vote_counts.get(player, 0))
            + " vote(s)"
        )


def day_phase(alive, roles, user_name, suspicions):
    print("DAY")
    print()
    print("Living players:")

    for player in alive:
        print(player)

    input("\nPress Enter to vote. The robots will vote automatically.")

    hide_screen()

    votes = collect_votes(
        alive,
        alive,
        roles,
        user_name,
        suspicions
    )

    leaders = top_voters(votes)

    show_vote_results(alive, votes)

    if len(leaders) == 1:
        eliminated = leaders[0]

        print()
        print(eliminated + " received the most votes.")

        input("Press Enter to eliminate this player.")

        eliminate_player(
            eliminated,
            alive,
            roles,
            user_name,
            "the village vote"
        )

        return

    if not leaders:
        print("Nobody received a valid vote.")
        print("Nobody is eliminated today.")

        input("Press Enter to continue.")

        hide_screen()

        return

    print()
    print("The vote is tied between: " + ", ".join(leaders))

    input("Press Enter for a revote between these players.")

    hide_screen()

    revotes = collect_votes(
        alive,
        leaders,
        roles,
        user_name,
        suspicions
    )

    revote_leaders = top_voters(revotes)

    show_vote_results(alive, revotes)

    if len(revote_leaders) == 1:
        eliminated = revote_leaders[0]

        print()
        print(eliminated + " received the most votes in the revote.")

        input("Press Enter to eliminate this player.")

        eliminate_player(
            eliminated,
            alive,
            roles,
            user_name,
            "the revote"
        )

    else:
        print("The revote is tied again.")
        print("Nobody is eliminated today.")

        input("Press Enter to continue.")


def show_final_result(winner, players, roles, alive, user_name):
    hide_screen()

    print("GAME OVER")
    print()

    if winner == "Village":
        print("THE VILLAGE WINS!")

    else:
        print("THE WEREWOLVES WIN!")

    if user_name in alive:
        print("You survived as " + user_name + ".")

    else:
        print("Your player " + user_name + " was eliminated.")

    print()
    print("SURVIVING PLAYERS")

    if alive:
        for player in alive:
            print(player)

    else:
        print("Nobody survived.")

    print()
    print("ALL ROLES")

    for player in players:
        print(player + ": " + roles[player])


def main():
    players, user_name = choose_player_name()

    roles = assign_roles(players)

    alive = players.copy()

    last_protected = None

    suspicions = {
        player: 0 for player in players
    }

    reveal_user_role(user_name, roles, players)

    while True:

        winner = check_winner(alive, roles)

        if winner is not None:
            break

        last_protected = night_phase(
            alive,
            roles,
            user_name,
            last_protected,
            suspicions
        )

        winner = check_winner(alive, roles)

        if winner is not None:
            break

        day_phase(
            alive,
            roles,
            user_name,
            suspicions
        )

        winner = check_winner(alive, roles)

        if winner is not None:
            break

    show_final_result(
        winner,
        players,
        roles,
        alive,
        user_name
    )


main()
