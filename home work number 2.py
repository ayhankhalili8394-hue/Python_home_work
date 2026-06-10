R1 = int(input("tell me a number for R1: "))
R2 = int(input("tell me a number for R2: "))
R3 = int(input("tell me a number for R3: "))

R = ((R1 * R2 * R3) / ((R1 * R2) + (R2 * R3) + (R1 * R3)))

print(R)