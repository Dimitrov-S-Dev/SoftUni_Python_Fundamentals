# Task 1 Extract Person Information

# def get_text(text):
#     name = ""
#     age = ""
#     name_start = text.index("@") + 1
#     name_end = text.index("|")
#     name += text[name_start:name_end]
#     age_start = text.index("#") + 1
#     age_end = text.index("*")
#     age += text[age_start:age_end]
#     print(f"{name} is {age} years old.")
#
#
# def get_name_age(number):
#     for _ in range(n):
#         current_text = input()
#         get_text(current_text)
#
#
# n = int(input())
# get_name_age(n)

# Task 2 ASCII Sumator

# def get_main(txt,begin, end):
#     result = 0
#
#     for char in txt:
#         if ord(char) in range(begin, end):
#             result += ord(char)
#
#     return result
#
#
# start = ord(input())
# end = ord(input())
# text = input()
# print(get_main(text, start, end))

# Task 3 Treasure Finder
#
# def get_type(txt):
#     type = ""
#     start = False
#     for elem in txt:
#         if elem == "&":
#             if start:
#                 break
#             else:
#                 start = True
#             continue
#         if start:
#             type += elem
#     return type
#
#
# def get_coordinates(txt):
#     coordinate = ""
#     start_type = txt.index("<") + 1
#     end_type = txt.index(">")
#     coordinate += txt[start_type:end_type]
#     return coordinate

#
# def get_main(lst):
#     while True:
#         text = input()
#         if text == "find":
#             break
#         result = ""
#         count = 0
#         for char in text:
#             result += chr((ord(char) - lst[count]))
#             count += 1
#             if count == len(lst):
#                 count = 0
#
#         type = get_type(result)
#         cordinates = get_coordinates(result)
#         print(f"Found {type} at {cordinates}")
#
#
# key = [int(x) for x in input().split()]
# get_main(key)


