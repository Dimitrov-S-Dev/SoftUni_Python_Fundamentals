amounts = [int(x) for x in input().split(', ')]
beggars = int(input())
result = []

for beggar in range(beggars):
    curr_amount = 0
    for index in range(beggar, len(amounts), beggars):
        curr_amount += amounts[index]
    result.append(curr_amount)

print(result)
