number_of_orders = int(input())

t_price = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue
    coffe_price = price_per_capsule * days * capsules
    t_price += coffe_price
    print(f"The price for the coffee is: ${coffe_price:.2f}")

print(f"Total: ${t_price:.2f}")
