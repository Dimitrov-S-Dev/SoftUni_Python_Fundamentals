WATER_TANK = 255
water_filled = 0
n = int(input())


for _ in range(n):
    curr_liters = int(input())
    if curr_liters > WATER_TANK - water_filled:
        print('Insufficient capacity!')
        continue
    water_filled += curr_liters

print(water_filled)
