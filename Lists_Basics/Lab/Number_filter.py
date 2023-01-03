count_iter = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
numbers = []

for _ in range(count_iter):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []
for num in numbers:
    filtered_pass = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filtered_pass:
        filtered_numbers.append(num)

print(filtered_numbers)
