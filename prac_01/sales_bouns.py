"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

VALID_SALES = 0
SALES_BOUNDARY = 1000
LOW_BONUS_RATE = 0.10
HIGH_BONUS_RATE = 0.15

sales = float(input("Enter sales: $"))

while sales >= VALID_SALES:
    if sales >= SALES_BOUNDARY:
        bonus_rate = LOW_BONUS_RATE
    else:
        bonus_rate = HIGH_BONUS_RATE
    bonus = sales * bonus_rate
    print(int(bonus))
    sales = float(input("Enter sales: $"))

print("do next thing")
