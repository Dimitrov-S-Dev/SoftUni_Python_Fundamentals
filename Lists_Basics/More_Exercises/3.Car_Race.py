numbers = [int(x) for x in input().split()]
middle = len(numbers) // 2
left_side = numbers[: middle]
right_side = numbers[middle + 1:]


left_time = 0
right_time = 0

for time in left_side:
    if time == 0:
        left_time *= 0.8
    else:
        left_time += time

for time in right_side[::-1]:
    if time == 0:
        right_time *= 0.8
    else:
        right_time += time

total_time = min(left_time, right_time)
print(f"The winner is {'left' if left_time < right_time else 'right'} with total time: {total_time:.1f}")
