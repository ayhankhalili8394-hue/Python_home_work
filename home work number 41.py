import time

print("Stopwatch")

for round_num in range(1, 4):
    input(f"\nPress Enter to start Round {round_num}...")

    print(f"Round {round_num} started!")

    for second in range(1, 6):
        print("Second:", second)
        time.sleep(1)

    print(f"Round {round_num} finished!")

print("\nAll 3 rounds are complete!")