import re

pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"
n = int(input())

for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if matches:
        numbers = []
        for char in matches[0][1]:
            numbers.append(str(ord(char)))
        print(f"{matches[0][0]}: {' '.join(numbers)}")
    else:
        print("The message is invalid")
