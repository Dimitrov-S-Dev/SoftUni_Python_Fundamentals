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
