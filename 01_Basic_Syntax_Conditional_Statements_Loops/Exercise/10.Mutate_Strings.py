first = input()
second = input()
result = first

for i in range(len(first)):
    if first[i] == second[i]:
        continue
    result = second[:i + 1] + first[i + 1:]
    print(result)
