# Get input from the user
income = float(input("Enter your monthly income (USD): "))
married = input("Are you married? (yes/no): ").lower()

# Determine the tax rate
if income > 50000:
    tax_rate = 20
elif income >= 30000:
    tax_rate = 15
elif income >= 10000:
    tax_rate = 10
else:
    tax_rate = 0

# Reduce tax rate by 2% if married
if married == "yes" and tax_rate > 0:
    tax_rate -= 2

# Calculate the final tax amount
tax = income * (tax_rate / 100)

# Display the result
print("Tax rate:", tax_rate, "%")
print("Final tax amount: $", tax)