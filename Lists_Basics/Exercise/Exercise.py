# Task 5 Mid-Exam-Preparation Faro Shuffle

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

# Task 6 Survival of the Biggest

numbers = list(map(int, input().split()))
remove_count = int(input())
result = sorted(numbers, reverse=True)

for _ in range(remove_count):
    num = result.pop()
    numbers.remove(num)

print(*numbers, sep=',')

# Task 7 Easter Gifts

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

# Task 8 Seize the Fire

level_of_fire = input().split('#')
water = int(input())
""" 
type_of_fire -> water_amount:
high -> 81 - 125
medium -> 51 - 80
low -> 1 - 50
"""
effort = 0
total_fire = 0
condition = True
print('Cells:')

for level in level_of_fire:
    info = level.split(' = ')
    fire_type = info[0]
    fire_value = int(info[1])
    condition = False
    if fire_type == 'High':
        if 81 <= fire_value <= 125:
            condition = True
    elif fire_type == 'Medium':
        if 51 <= fire_value <= 80:
            condition = True
    elif fire_type == 'Low':
        if 1 <= fire_value <= 50:
            condition = True
    if condition:
        if water >= fire_value:
            water -= fire_value
            effort += fire_value * 0.25
            total_fire += fire_value
            print(f"- {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

# Task 9 Hello, France

train_ticket = 150
items = input().split('|')
budget = float(input())
profit = 0
new_price = []
"""
clothes = 50.00
shoes = 35.00
accessories = 20.50
"""
condition = False
for item in items:
    info = item.split('->')
    item_type = info[0]
    price = float(info[1])
    condition = False
    if item_type == 'Clothes' and price <= 50:
        condition = True
    elif item_type == 'Shoes' and price <= 35:
        condition = True
    elif item_type == 'Accessories' and price <= 20.5:
        condition = True
    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.4
            rounded_price = round(price * 1.4, 2)
            new_price.append(rounded_price)

print(*new_price, sep=" ")
print(f"Profit: {profit:.2f}")
sum_of_all = sum(new_price)

if sum_of_all + budget > 150:
    print('Hello, France!')
else:
    print('Not enough money.')

# Task 10 Bread Factory

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
            print(f"Closed! Cannot afford {order}.")
            is_bakery_closed = True
            break
if not is_bakery_closed:
    print('Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
