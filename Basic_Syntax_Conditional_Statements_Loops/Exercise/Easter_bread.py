budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = flour_price * 1.25
bread_price = flour_price + eggs_price + (milk_price / 4)
bread_count = 0
colored_eggs = 0

while budget >= bread_price:
	bread_count += 1
	budget -= bread_price
	colored_eggs += 3
	if bread_count % 3 == 0:
		if colored_eggs > bread_count - 2:
			colored_eggs -= bread_count - 2
		else:
			break
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
