import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
number = r"\d"
n = int(input())
for _ in range(n):
    text = input()
    match = re.search(pattern, text)
    if match:
        group = re.findall(number, match.group())
        if group:
            print(f"Product group: {''.join(group)}")
        else:
            print(f"Product group: 00")
    else:
        print(f"Invalid barcode")
