# Task 1 Race

import re
#
# names = input().split(", ")
# names_dict = {}
#
# for name in names:
#     names_dict[name] = 0
#
# while True:
#     distance = 0
#     text = input()
#     if text == "end of race":
#         break
#
#     name_pattern = r"[A-Za-z]"
#     distance_pattern = r"\d"
#     name_match = re.findall(name_pattern, text)
#     p_name = "".join(name_match)
#     distance_match = re.findall(distance_pattern, text)
#     if p_name not in names_dict.keys():
#         continue
#     for digit in distance_match:
#         distance += int(digit)
#     names_dict[p_name] += distance
#
# x = {k: v for k, v in sorted(names_dict.items(), key=lambda item: item[1], reverse=True)}
# count = 0
# for k in x.keys():
#     count += 1
#     if count == 1:
#         print(f"1st place: {k}")
#     elif count == 2:
#         print(f"2nd place: {k}")
#     else:
#         print(f"3rd place: {k}")
#     if count == 3:
#         break

# Task 2 SoftUni Bar Income
barcode_dict = {}

while True:
    text = input()
    if text == "end of shift":
        break
    pattern = r"%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9](?=\$))"
    matches = re.finditer(pattern, text)
    if matches:
        for match in matches:
            name = match.group(1)
            product = match.group(2)
            qty = int(match.group(3))
            price = float(match.group(4))
            if name not in barcode_dict.keys():
                barcode_dict[name]= {product: 0}
            total_price = qty * price
            barcode_dict[name][product] += total_price
            print(f"{name}: {product} - {total_price:.2f}")

total = 0
for k,v in barcode_dict.items():
    for sub_k in v.keys():
        total += barcode_dict[k][sub_k]
print(f"Total income: {total:.2f}")
