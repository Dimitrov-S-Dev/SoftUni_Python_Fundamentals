# Task 1 Secret Chat

# def get_while(message):
#     while True:
#         command = input()
#         if command == "Reveal":
#             break
#         info = command.split(":|:")
#         action = info[0]
#
#         if action == "InsertSpace":
#             index = int(info[1])
#             message = message[0:index] + " " + message[index:]
#             print(message)
#
#         elif action == "Reverse":
#             substring = info[1]
#             if substring in message:
#                 message = message.replace(substring, "", 1)
#                 message += substring[::-1]
#                 print(message)
#             else:
#                 print(f"error")
#
#         elif action == "ChangeAll":
#             substring = info[1]
#             replacement = info[2]
#             message = message.replace(substring, replacement)
#             print(message)
#
#     return message
#
#
# def get_print(message):
#     print(f"You have a new text message: {message}")
#
# def get_secret_chat(message):
#     message = get_while(message)
#     get_print(message)
#
#
# data = input()
# get_secret_chat(data)

# Task 2 Emoji Detector

import re

emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
numbers_pattern = r"(\d)"
text = input()

threshold = 1
e_matches = re.findall(emoji_pattern, text)
n_matches = re.findall(numbers_pattern, text)

for num in n_matches:
    threshold *= int(num)
cool_emoji = []
for elem in e_matches:
    cur_sum = 0
    for char in elem[1]:
        cur_sum += ord(char)
    if cur_sum > threshold:
        cool_emoji.append(elem)
print(f"Cool threshold: {threshold}")
print(f"{len(e_matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emoji:
    print(''.join(emoji), end=" \n")


