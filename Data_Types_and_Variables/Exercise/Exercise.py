# Task 7 Water Overflow

count_iter = int(input())
max_capacity = 255
capacity = 0

for _ in range(count_iter):
    letters = int(input())
    if letters + capacity > max_capacity:
        print("Insufficient capacity!")
        continue
    capacity += letters

print(capacity)

# Task 8 Party Profit

group_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    if day % 3 == 0:
        coins -= group_size * 3
    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:
            coins -= group_size * 2
    coins += 50
    coins -= group_size * 2

avg_coins = coins // group_size
print(f"{group_size} companions received {avg_coins} coins each.")

# Task 9 Snowballs

snowballs_count = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quantity = 0

for balls in range(snowballs_count):
    ball_weight = int(input())
    ball_time = int(input())
    ball_quality = int(input())
    ball_value = (ball_weight / ball_time) ** ball_quality
    if ball_value > max_value:
        max_value = ball_value
        max_weight = ball_weight
        max_time = ball_time
        max_quantity = ball_quality

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quantity})")

# Task 10 Gladiator Expenses

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_breaks = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 6 == 0:
        expenses += shield_price
        shield_breaks += 1
        if shield_breaks % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
