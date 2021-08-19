"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Shop Calculator

Pseudocode:

DISCOUNT_BRACKET = 100
total = 0
total_items = get user input as an int
if total_items < = 0
    display "Invalid: Must enter at least one item"
    total_items = get user input as an int
for i in total_items
    get user input of each item price
    += total
if total >= DISCOUNT_BRACKET
    display total - total * 0.1
else:
    display total

"""


DISCOUNT_BRACKET = 100
total = 0
total_items = int(input("Enter number of items purchased: "))
if total_items <= 0:
    print("Invalid: Must enter at least one item")
    total_items = int(input("Enter number of items purchased: "))
for i in range(total_items):
    item_price = float(input("Enter item price: "))
    total += item_price
if total >= DISCOUNT_BRACKET:
    print("Total with discount: ${:.2f}".format(total - total * 0.1))
else:
    print(("Total: ${:.2f}".format(total)))

