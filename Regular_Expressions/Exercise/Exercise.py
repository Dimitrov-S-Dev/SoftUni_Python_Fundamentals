import re
# Task 1 Capture the Numbers
pattern = r"\d+"

text = input()
while text:
    match = re.findall(pattern, text)
    if match:
        print(" ".join(match),end=" ")
    text = input()

# Task 2 Find Variable Names in Sentences

pattern = r"\b\_[A-Za-z0-9]+\b"
text = input()

matches = re.findall(pattern, text)
result = []
for match in matches:
    result.append(match[1:])
print(",".join(result),end="")

# Task 3 Find Occurrences of Word in Sentence

text = input()
pattern = input()

match = re.findall(pattern, text, re.IGNORECASE)
print(len(match))

# Task 4 Extract Email

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"

text = input()

matches = re.findall(pattern, text)
for match in matches:
    print(match[0])

# Task 5 Furniture

bought_furniture = []
total_sum = 0

pattern = r"(?P<name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)\!(?P<qty>\d+)"

while True:
    command = input()
    if command == "Purchase":
        break
    maches = re.finditer(pattern, command)
    if maches:
        for mach in maches:
            name = mach.group("name")
            bought_furniture.append(name)
            price = float(mach.group("price"))
            qty = int(mach.group("qty"))
            total_sum += price * qty
print(f"Bought furniture:")
for elem in bought_furniture:
    print(elem)
print(f"Total money spend: {total_sum:.2f}")


# Task 6 Extract the Links

pattern = r"(www\.[a-zA-Z]+([a-zA-Z0-9\-]+)*(\.[a-z]+)+)"
valid_emails = []

while True:
    text = input()
    if not text:
        break
    matches = re.finditer(pattern, text)
    if matches:
        for match in matches:
            valid_emails.append(match.group(0))


for valid in valid_emails:
    print(valid)
