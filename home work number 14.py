# Get room information
price = float(input("Enter the room price per night: "))
nights = int(input("Enter the number of nights: "))

adults = int(input("Enter the number of adults (18+): "))
teenagers = int(input("Enter the number of teenagers (3-17): "))
children = int(input("Enter the number of children (under 3): "))

# Check if children use hotel services
service = input("Do the children use hotel services? (yes/no): ").lower()

# Count people (children are NOT counted for capacity)
total_people = adults + teenagers

# Validation
if total_people < 1:
    print("Error: At least one adult or teenager is required.")
elif total_people > 7:
    print("Error: The maximum room capacity is 7 people.")
elif adults == 0:
    print("Error: People under 18 cannot stay without an adult.")
else:
    # Calculate cost
    total_cost = (adults * price) + (teenagers * price)

    if service == "yes":
        total_cost += children * (price / 2)
    # If service == "no", children stay for free

    total_cost *= nights

    print("Total cost:", total_cost)


