# Task 1 Activation Keys

# def get_contains(text, sub_text):
#     if sub_text in text:
#         print(f"{text} contains {sub_text}")
#     else:
#         print(f"Substring not found!")
#
#
# def get_flip(text, command, start, end):
#     if command == "Upper":
#         text = text[0:start] + text[start:end].upper() + text[end:]
#
#     elif command == "Lower":
#         text = text[0:start] + text[start:end].lower() + text[end:]
#     print(text)
#     return text
#
# def get_slice(text, start, end):
#     text = text[0:start] + text[end:]
#     print(text)
#     return text
# def get_while(text):
#     while True:
#         command = input()
#         if command == "Generate":
#             break
#         info = command.split(">>>")
#         action = info[0]
#
#         if action == "Contains":
#             substring = info[1]
#             get_contains(text, substring)
#         elif action == "Flip":
#             upper_lower = info[1]
#             start_index = int(info[2])
#             end_index = int(info[3])
#             text = get_flip(text,upper_lower, start_index, end_index)
#         elif action == "Slice":
#             start_index = int(info[1])
#             end_index = int(info[2])
#             text = get_slice(text, start_index, end_index)
#     print(f"Your activation key is: {text}")
#
# def get_activation_keys(text):
#     text = get_while(text)
#
# data = input()
# get_activation_keys(data)

# Task 2

import re
n = int(input())
for _ in range(n):
    curr_barcode = input()
    pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])"
    match = re.search(pattern, curr_barcode)
    if match:
       num = r"\d"
       numbers = re.findall(num, match.group())
       if numbers:
           print(f"Product group: {''.join(numbers)}")
       else:
           print(f"Product group: 00")
    else:
        print(f"Invalid barcode")

# Task 3


