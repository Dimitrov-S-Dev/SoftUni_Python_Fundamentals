# numbers = list(map(int, input().split()))
# print([-el for el in numbers])

string = input().split()
result = []

for el in string:
    current_elem = -int(el)
    result.append(current_elem)

print(result)
