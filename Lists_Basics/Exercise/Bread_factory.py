events = input().split('|')
energy = 100
coins = 100
is_bakery_closed = False
for event in events:
    info = event.split('-')
    order = info[0]
    number = int(info[1])
    if order == 'rest':
        current_energy = energy
        if current_energy + number > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = number
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif order == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {order}.")
        else:
            print(f"Closed! You cannot afford {order}.")
            is_bakery_closed = True
            break
if not is_bakery_closed:
    print('Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




