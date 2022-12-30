decoration_quantity = int(input())
days_to_christmas = int(input())
ornament_price, ornament_points = 2, 5
skirt_price, skirt_points = 5, 3
garland_price, garland_points = 3, 10
lights_price, lights_points = 15, 17
points = 0
money = 0
for day in range(1, days_to_christmas + 1):
	if day % 11 == 0:
		decoration_quantity += 2
	if day % 10 == 0:
		points -= 20
		money += skirt_price + garland_price + lights_price
	if day % 5 == 0:
		money += lights_price * decoration_quantity
		points += lights_points
		if day % 3 == 0:
			points += 30
	if day % 3 == 0:
		money += (skirt_price + garland_price) * decoration_quantity
		points += skirt_points + garland_points
	if day % 2 == 0:
		money += ornament_price * decoration_quantity
		points += ornament_points

if days_to_christmas % 10 == 0:
	points -= 30

print(f"Total cost: {money}")
print(f"Total points: {points}")


