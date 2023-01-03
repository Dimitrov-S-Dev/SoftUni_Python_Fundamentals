easter_gifts = input().split()

command = input()
while command != 'No Money':
    info = command.split()
    action = info[0]
    gift_name = info[1]
    if action == 'OutOfStock':
        if gift_name in easter_gifts:
            for index, elem in enumerate(easter_gifts):
                if elem == gift_name:
                    easter_gifts[index] = 'None'
    elif action == 'JustInCase':
        easter_gifts[-1] = gift_name
    else:
        idx = int(info[2])
        if idx in range(len(easter_gifts)):
            easter_gifts[idx] = gift_name
    command = input()

for gift in easter_gifts:
    if gift == 'None':
        easter_gifts.remove(gift)
print(*easter_gifts)
