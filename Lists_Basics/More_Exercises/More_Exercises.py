# Task 1 Zeros to Back

numbers = list(map(int, input().split(', ')))
zeros = []

for index in range(len(numbers) - 1, -1, -1):
    if numbers[index] == 0:
        zero = numbers.pop(index)
        zeros.append(zero)
result = numbers + zeros
print(result)

# Task 2 Messaging

numbers = input().split()
text = input()
message = []

for num in numbers:
    index_sum = 0
    for digit in num:
        index_sum += int(digit)
    index_sum %= len(text)

    message.append(text[index_sum])
    text = text.replace(text[index_sum], '', 1)
print(message)

# Task 3 Car Race

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
    print(f"The winner is the left with total time:{sum_lst(left):.1f}")
else:
    print(f"The winner is the right with total time:{sum_lst(right):.1f}")

# Task 4 Josephus Permutation

people = list(map(int, input().split()))
kill_count = int(input())
result = []
counter = 0
index = 0

while len(people) > 0:
    counter += 1
    if counter % kill_count == 0:
        result.append(people.pop(index))
    else:
        index += 1
    if index >= len(people):
        index = 0
print(result)
