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
