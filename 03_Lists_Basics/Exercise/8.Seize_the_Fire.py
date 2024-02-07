fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0

print('Cells:')

for fire in fires:
    fire_type, value = fire.split(' = ')
    value = int(value)

    if fire_type == 'High' and (value < 81 or value > 125):
        continue

    elif fire_type == 'Medium' and (value < 51 or value > 80):
        continue
    elif fire_type == 'Low' and (value < 1 or value > 50):
        continue

    if water >= value:
        water -= value
        total_fire += value
        effort += value * 0.25
        print(f'- {value}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
