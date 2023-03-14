# Task 1 World Tour

# def get_add(string, i, element):
#     if i in range(len(string)):
#         string = string[0:i] + element + string[i:]
#     return string
#
# def get_remove(string, start_i, end_i):
#     if start_i in range(len(string)) and end_i in range(len(string)):
#         string = string[0:start_i] + string[end_i + 1:]
#     return string
#
# def get_switch(string, old, new):
#     if old in string:
#         string = string.replace(old, new)
#     return string
#
#
# def get_word_tour(text):
#     while True:
#         command = input()
#         if command == "Travel":
#             break
#         info = command.split(":")
#         action = info[0]
#
#         if action == "Add Stop":
#             index = int(info[1])
#             word = info[2]
#             text = get_add(text, index, word)
#         elif action == "Remove Stop":
#             start_index = int(info[1])
#             end_index = int(info[2])
#             text = get_remove(text, start_index, end_index)
#         elif action == "Switch":
#             old_str = info[1]
#             new_str = info[2]
#             text = get_switch(text, old_str, new_str)
#         print(text)
#
#     print(f"Ready for world tour! Planned stops: {text}")
#
# data = input()
# get_word_tour(data)


# Task 2 Mirror Words

# import re
#
# pattern = r"(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
# text = input()
# pairs = []
# flag = 0
# matches = re.findall(pattern, text)
# if matches:
#     flag = 1
#     for match in matches:
#         if match[1] == match[-1][::-1]:
#             pairs.append(f"{match[1]} <=> {match[-1]}")
#
# else:
#     print(f"No word pairs found!")
# if flag:
#     if pairs:
#         print(f"{len(matches)} word pairs found!")
#         print(f"The mirror words are:")
#         for elem in pairs:
#             print(elem)
#
#     else:
#         print(f"No mirror words!")
