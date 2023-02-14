price = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        continue
    if current_price == 0:
        print("Invalid order!")
        continue
    price += float(command)

tax = price * 0.2
if price == 0:
    print(f"Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    total_price = price + tax
    if command == "special":
        total_price *= 0.9
    print(f"Total price: {total_price:.2f}$")
