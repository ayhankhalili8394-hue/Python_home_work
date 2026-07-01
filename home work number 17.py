# Get input from the user
price = int(input("Enter the payment amount (Tomans): "))
weight = float(input("Enter the product weight (kg): "))

# Check if the product qualifies for free shipping
if price > 1000000 and weight < 5:
    print("The order qualifies for free shipping.")
else:
    print("The order does not qualify for free shipping.")