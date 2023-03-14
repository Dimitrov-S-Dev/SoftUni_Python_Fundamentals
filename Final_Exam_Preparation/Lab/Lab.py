# Task 1 Secret Chat

# def get_insert(word, i):
#     word = word[0:i] + " " + word[i:]
#     return word
#
# def get_reverse(word, sub_word):
#     if sub_word in word:
#         word = word.replace(sub_word,sub_word[::-1])
#     else:
#         print("error")
#     return word
#
#
# def get_change(word, search_elem, replace_elem):
#     new_word = ""
#     for elem in word:
#         if elem == search_elem:
#             new_word += replace_elem
#         else:
#             new_word += elem
#     return new_word
#
#
# def get_secret_char(message):
#     while True:
#         command = input()
#         if command == "Reveal":
#             break
#         info = command.split(":|:")
#         action = info[0]
#
#         if action == "InsertSpace":
#             index = int(info[1])
#             message = get_insert(message, index)
#         elif action == "Reverse":
#             substring = info[1]
#             message = get_reverse(message, substring)
#         elif action == "ChangeAll":
#             substring = info[1]
#             replacement = info[2]
#             message = get_change(message, substring, replacement)
#
#     print(f"You have a new message message: {message}")
#
#
# data = input()
# get_secret_char(data)

# Task 2 Destination Mapper

import re

pattern = r"(?P<sep>[\=\/])?(?P<dest>[A-Z][]a-z]+)\1"
text = input()
destinations = []
travel_points = 0

matches = re.finditer(pattern, text)
for match in matches:
    destinations.append(match.group("dest"))
    travel_points += len(match.group("dest"))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")

