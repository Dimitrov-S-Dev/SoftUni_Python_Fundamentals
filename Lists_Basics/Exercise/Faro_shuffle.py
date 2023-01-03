cards = input().split()
shuffles = int(input())
middle = len(cards) // 2

for shuffle in range(shuffles):
    result = []
    top = cards[:middle]
    bottom = cards[middle:]
    for idx in range(middle):
        result.append(top[idx])
        result.append(bottom[idx])
    cards = result

print(result)
