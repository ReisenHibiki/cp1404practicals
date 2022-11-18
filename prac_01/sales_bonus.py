"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.1
    else
        bonus = sales * 0.15
    display bonus
    get sales

display Thank you for using the program!
"""

NUMBER_OF_SALES = 1000
BONUS_UNDER_1000 = 0.1
BONUS_ABOVE_1000 = 0.15

sales = float(input("Enter sales(enter negative number to stop): $"))

while sales >= 0:
    if sales < NUMBER_OF_SALES:
        bonus = sales * BONUS_UNDER_1000
    else:
        bonus = sales * BONUS_ABOVE_1000

    print(f"Your bonus is {bonus}")
    sales = float(input("Enter sales(enter negative number to stop): $"))

print("Thank you for using the program!")



