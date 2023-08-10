WATER_TANK = 255
water_filled = 0
n = int(input())


for _ in range(n):
    curr_liters = int(input())
    if curr_liters + water_filled > WATER_TANK:
        print('Insufficient capacity!')
        continue
    water_filled += curr_liters

print(water_filled)
