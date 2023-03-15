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

# import re
#
# words = {}
# name_pattern = r"\s([:*]{2})([A-Z][a-z]+)\1"
# number_pattern = r"\d"
# text = input()
# animals = []
# count = 1
# name_result = re.finditer(name_pattern, text)
# for name in name_result:
#     a_name = name.group(0)[1:]
#     animals.append(a_name)
#
# number_result = re.findall(number_pattern, text)
# if number_result:
#    count_int = [int(x) for x in number_result]
#    for num in count_int:
#        count *= num
#
# cool_animals = []
# for animal in animals:
#     curr_sum = 0
#     for char in animal:
#         curr_sum += ord(char)
#     if curr_sum > count:
#         cool_animals.append(animal)
# print(f"Cool threshold: {count}")
# print(f"{len(animals)} emojis found in the text. The cool ones are:")
# for anim in cool_animals:
#     print(f"{anim }")





