"""
CP1404/CP5632 - Practical
Samuel Barrett - 13038579

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:

BONUS_BRACKET = 1000.00
sales = get user input as a float in $
while sales > 0
    if sales < 1000
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    display bonus to 2 decimals places
    sales = get user input as a float in $
display "Thank-you"

"""

BONUS_BRACKET = 1000.00
sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < BONUS_BRACKET:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus = ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Thank-you")

