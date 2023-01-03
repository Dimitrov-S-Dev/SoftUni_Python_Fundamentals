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
