"""
get number_of_items
while number_of_items < 0
    display Invalid number of items!
    get number_of_items

for j from 0 to number_of_items
    get price_of_item
    total_price = total_price + price_of_item

if total_price > 100
    total_price = total_price * 0.9
display total_price
"""

BOUNDARY_OF_PRICE = 100
DISCOUNT_RATE = 0.9
BOUNDARY_OF_ITEM = 0
INITIALIZED_NUMBER = 0

total_price = INITIALIZED_NUMBER
number_of_items = int(input("Number of items: "))
while number_of_items < BOUNDARY_OF_ITEM:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for j in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > BOUNDARY_OF_PRICE:
    total_price *= DISCOUNT_RATE

print(f"Total price for 3 items is ${total_price:.2f}")
