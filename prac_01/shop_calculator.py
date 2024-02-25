item_number = int(input("Number of items: "))
total_price = 0

while item_number <= 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))

for i in range(item_number):
    item_price = float(input("Price of item: "))
    total_price += item_price

print(f"Total price for {item_number} is ${total_price:.2f}")
