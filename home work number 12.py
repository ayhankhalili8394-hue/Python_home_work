price = eval(input("You are in a shop. just type the price please and we going to give you some discount: "))

if price < 5000000:
    discount = 0

elif price > 5000000 and price < 15000000:
    discount = 5

if price > 15000000:
    discount = 10

final_price = price * (100 - discount) / 100

print(price, " = price")
print(discount, " = your discount")
print(final_price, " = final price")