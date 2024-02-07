cards = input().split()
shuffles = int(input())
middle = len(cards) // 2

for shuffle in range(shuffles):
    first_deck = cards[: middle]
    second_deck = cards[middle:]
    current_deck = []
    for index in range(len(first_deck)):
        current_deck.append(first_deck[index])
        current_deck.append(second_deck[index])

    cards = current_deck

print(cards)
