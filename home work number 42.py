import random

score = 0

for i in range(1, 21):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    user = int(input(f"Question {i}: {num1} {op} {num2} = "))

    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("The correct answer is", answer)

print("Your score is", score, "out of 20")

