x = 10

def change():
    global x
    x = 20

print("Before:", x)

change()

print("After:", x)