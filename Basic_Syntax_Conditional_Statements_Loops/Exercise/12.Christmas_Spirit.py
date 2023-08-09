quantity = int(input())
days = int(input())

budget = 0
totalSpirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 10 == 0:
        totalSpirit -= 20
        budget += 5 + 3 + 15

    if day % 2 == 0:
        budget += 2 * quantity
        totalSpirit += 5

    if day % 3 == 0:
        budget += 8 * quantity
        totalSpirit += 13

    if day % 5 == 0:
        budget += 15 * quantity
        totalSpirit += 17
        if day % 3 == 0:
            totalSpirit += 30


if days % 10 == 0:
    totalSpirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
