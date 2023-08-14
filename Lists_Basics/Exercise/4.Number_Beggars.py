moneys = list(map(int, input().split(', ')))
beggars_count = int(input())
result = []

for beggar in range(beggars_count):
    beggar_amount = 0
    for idx in range(beggar, len(moneys), beggars_count):
        beggar_amount += moneys[idx]
    result.append(beggar_amount)

print(result)

'''
numbers = input().split(', ')
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):
    beggar_idx = idx % beggars_count
    num = numbers[idx]
    beggars[beggar_idx] += num
    
print(beggars)
'''