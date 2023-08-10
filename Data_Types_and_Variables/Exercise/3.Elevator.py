people = int(input())
capacity = int(input())
count = 0
if capacity != 0:
    for number in range(0, people, capacity):
        count += 1

print(count)
