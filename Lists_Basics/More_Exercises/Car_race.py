def sum_lst(lst):
    total = 0
    for num in lst:
        if num == 0:
            total *= 0.8
        total += num
    return total


time = list(map(int, input().split()))
middle = len(time) // 2
left = time[:middle]
right = time[middle:]

if sum_lst(left) < sum_lst(right):
    print(f"The winner is the left with total time: {sum_lst(left):.1f}")
else:
    print(f"The winner is the right with total time: {sum_lst(right):.1f}")
