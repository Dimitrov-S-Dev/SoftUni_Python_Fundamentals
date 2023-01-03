count_iter = int(input())
max_capacity = 255
capacity = 0

for _ in range(count_iter):
    letters = int(input())
    if letters + capacity > max_capacity:
        print("Insufficient capacity!")
        continue
    capacity += letters

print(capacity)
