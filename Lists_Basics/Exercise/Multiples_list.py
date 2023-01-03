factor = int(input())
count = int(input())
result = []

for number in range(1, count + 1):
    current_num = number * factor
    result.append(current_num)

print(result)
