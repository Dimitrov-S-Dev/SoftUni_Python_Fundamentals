numbers = list(map(int, input().split(', ')))
result = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(result)

