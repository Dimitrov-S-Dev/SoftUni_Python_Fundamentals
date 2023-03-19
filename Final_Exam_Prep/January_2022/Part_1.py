# Task 1 The Limitation Game

# def get_while(string):
#     while True:
#         command = input()
#         if command == "Decode":
#             break
#         info = command.split("|")
#         action = info[0]
#
#         if action == "Move":
#             num_letters = int(info[1])
#             string = string[num_letters:] + string[0:num_letters]
#         elif action == "Insert":
#             index = int(info[1])
#             value = info[2]
#             string = string[0:index] + value + string[index:]
#         elif action == "ChangeAll":
#             substring = info[1]
#             replacement = info[2]
#             string = string.replace(substring, replacement)
#     return string
#
#
# def get_print(string):
#     print(f"The decrypted message is: {string}")
#
# def get_limit_game(string):
#     string = get_while(string)
#     get_print(string)
#
#
# text = input()
# get_limit_game(text)
#

# Task 2 Destination Mapper

import re

pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
text = input()
destinations = []

matches = re.finditer(pattern, text)
for match in matches:
    destinations.append(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
length = 0
for elem in destinations:
    length += len(elem)
print(f"Travel Points: {length}")
