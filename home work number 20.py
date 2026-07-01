# Get the coordinates from the user
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

# Determine the quadrant
if x > 0 and y > 0:
    print("The point is in the First Quadrant.")
elif x < 0 and y > 0:
    print("The point is in the Second Quadrant.")
elif x < 0 and y < 0:
    print("The point is in the Third Quadrant.")
elif x > 0 and y < 0:
    print("The point is in the Fourth Quadrant.")
elif x == 0 and y == 0:
    print("The point is at the Origin.")
elif x == 0:
    print("The point is on the Y-axis.")
elif y == 0:
    print("The point is on the X-axis.")
else:
    print("Error")