count_iter = int(input())
total = 0
for _ in range(count_iter):
    current_char = input()
    total += ord(current_char)
print(f"The sum equals: {total}")
