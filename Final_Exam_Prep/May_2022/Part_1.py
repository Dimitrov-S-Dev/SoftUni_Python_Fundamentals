# Task 1 Password Reset

# def get_take(text):
#     new_text = ""
#     for i in range(len(text)):
#         if i % 2 != 0:
#             new_text += text[i]
#     print(new_text)
#     return new_text
#
#
# def get_cut(text, i, len):
#     start = i + len
#     text = text[0:i] + text[start:]
#     print(text)
#     return text
#
#
# def get_sub(text, elem, new_elem):
#     if elem in text:
#         text = text.replace(elem, new_elem)
#         print(text)
#     else:
#         print(f"Nothing to replace!")
#
#     return text
#
#
# def get_pass(string):
#     while True:
#         command = input()
#         if command == "Done":
#             break
#         info = command.split()
#         action = info[0]
#
#         if action == "TakeOdd":
#             string = get_take(string)
#         elif action == "Cut":
#             index = int(info[1])
#             length = int(info[2])
#             string = get_cut(string, index, length)
#         elif action == "Substitute":
#             word = info[1]
#             replace = info[2]
#             string = get_sub(string, word, replace)
#
#     print(f"Your password is: {string}")
#
# data = input()
# get_pass(data)
#

# Task 2 Emoji Detector
import re

text = input()
pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
matches = re.findall(pattern, text)

threshold = 1
for char in text:
    if char.isdigit():
        threshold *= int(char)

cool_emojis = []
for emoji in matches:
    coolnes = 0
    for char in emoji[1]:
        coolnes += ord(char)

    if coolnes > threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {threshold}')
if len(matches) > 0:
    print(f'{len(matches)} emojis found in the text. The cool ones are:')
    for emoji in cool_emojis:
        print(''.join(emoji))




