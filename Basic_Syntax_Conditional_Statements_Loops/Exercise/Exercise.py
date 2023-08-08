#
# Task 11 Easter Bread

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

# Task 12 Christmas Spirit

decoration_quantity = int(input())
days_to_christmas = int(input())
ornament_price, ornament_points = 2, 5
skirt_price, skirt_points = 5, 3
garland_price, garland_points = 3, 10
lights_price, lights_points = 15, 17
spirit = 0
money = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        decoration_quantity += 2
    if day % 10 == 0:
        spirit -= 20
        money += skirt_price + garland_price + lights_price
    if day % 5 == 0:
        money += lights_price * decoration_quantity
        spirit += lights_points
        if day % 3 == 0:
            spirit += 30
    if day % 3 == 0:
        money += (skirt_price + garland_price) * decoration_quantity
        spirit += skirt_points + garland_points
    if day % 2 == 0:
        money += ornament_price * decoration_quantity
        spirit += ornament_points

if days_to_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
