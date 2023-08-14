numbers = [int(x) for x in input().split(', ')]
result = []

numbers_no_zero = [x for x in numbers if x != 0]
zeros = [x for x in numbers if x == 0]
result.extend(numbers_no_zero)
result.extend(zeros)

print(result)
