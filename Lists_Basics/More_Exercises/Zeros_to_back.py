numbers = list(map(int, input().split(', ')))
zeros = []

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] == 0:
        zero = numbers.pop(index)
        zeros.append(zero)
result = numbers + zeros
print(result)
