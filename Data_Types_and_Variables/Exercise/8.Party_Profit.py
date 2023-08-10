companions_count = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 15 == 0:
        companions_count += 5
    if day % 10 == 0:
        companions_count -= 2
    coins += 50 - 2 * companions_count
    if day % 3 == 0:
        coins -= 3 * companions_count
    if day % 5 == 0:
        coins += 20 * companions_count
        if day % 3 == 0:
            coins -= 2 * companions_count

print(f'{companions_count} companions received {coins // companions_count} coins each.')
