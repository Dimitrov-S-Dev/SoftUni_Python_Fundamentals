import re

pattern = r"(#|\|)([A-Z a-z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
text = input()

matches = re.findall(pattern, text)
calories = 0
items = []

for match in matches:
    calories += int(match[3])
    items.append(match)

days = calories // 2000
print(f"You have food to last you for: {days} days!")
for item in items:
    print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")
