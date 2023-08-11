fight_count = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
shield_count = 0
expenses = 0

for fight in range(1, fight_count + 1):
    if fight % 2 == 0:
        expenses += helmet
    if fight % 3 == 0:
        expenses += sword

    if fight % 6 == 0:
        shield_count += 1
        if shield_count % 2 == 0:
            expenses += armor
        expenses += shield

print(f'Gladiator expenses: {expenses:.2f} aureus')
