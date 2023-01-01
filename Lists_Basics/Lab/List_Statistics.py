count_iter = int(input())
positive = []
negative = []

for _ in range(count_iter):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positive: {len(positive)}")
print(f"Count of negatives: {sum(negative)}")
