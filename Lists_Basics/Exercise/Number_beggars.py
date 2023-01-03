moneys = list(map(int, input().split(', ')))
beggars_count = int(input())
result = []

for beggar in range(beggars_count):
    beggar_amount = 0
    for idx in range(beggar, len(moneys), beggars_count):
        beggar_amount += moneys[idx]
    result.append(beggar_amount)

print(result)
