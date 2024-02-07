numbers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    curr_num = min(numbers)
    numbers.remove(curr_num)

print(*numbers, sep=', ')
