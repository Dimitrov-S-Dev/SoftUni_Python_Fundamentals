numbers = list(map(int, input().split()))
remove_count = int(input())
result = sorted(numbers, reverse=True)

for _ in range(remove_count):
    num = result.pop()
    numbers.remove(num)

print(*numbers, sep=',')
