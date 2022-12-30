orders_count = int(input())
total_price = 0
for order in range(orders_count):
	price_per_capsule = float(input())
	days = int(input())
	capsule_per_day = int(input())
	if 1 <= capsule_per_day <= 2000 and 1 <= days <= 31 and 0.01 <= price_per_capsule <= 100.00:
		price = price_per_capsule * days * capsule_per_day
		print(f"The price for the coffee is: ${price:.2f}")
		total_price += price

print(f"Total: ${total_price:.2f}")
