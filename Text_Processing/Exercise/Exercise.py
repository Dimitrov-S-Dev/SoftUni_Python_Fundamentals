# Task 1 Valid Usernames
# import string
#
# def get_main(lst):
#     expected_element = string.digits + string.ascii_letters + "-" + "_"
#     for name in lst:
#         condition = True
#         if 3 > len(name) or len(name) > 16:
#             condition = False
#         elif len([x for x in name if x in expected_element]) != len(name):
#             condition = False
#         elif condition:
#             print(name)
#
# username = input().split(", ")
# get_main(username)
import string


# Task 2 Character Multiplier

# def get_result(first, second):
#     total_sum = 0
#     for i in range(len(first)):
#         if i < len(second):
#             total_sum += ord(first[i]) * ord(second[i])
#         else:
#             total_sum += ord(first[i])
#     return total_sum
#
# def get_multiply(first_word, second_word):
#     result = 0
#     if len(first_word) > len(second_word):
#         result = get_result(first_word, second_word)
#     else:
#         result = get_result(second_word, first_word)
#     print(result)
#
#
# data = input().split()
# get_multiply(data[0],data[1])

# Task 3 Extract File

# def get_name(word):
#     name, extension = word.split(".")
#     result = f"File name: {name}"
#     result += f"\nFile extension: {extension}"
#     return result
#
# file = input().split("\\")
# print(get_name(file[-1]))

# Task 4 Caesar Cipher

# text = input()
# result = ""
#
# for char in text:
#     index = ord(char) + 3
#     result += chr(index)
#
# print(result)

# Task 5 Emoticon Finder

# text = input("")
#
# for index in range(len(text)):
#     if text[index] == ":":
#         print(f"{text[index]}{text[index + 1]}")

# Task 6  Replace Repeating Chars

# def get_result(word):
#     result = word[0]
#     for char in word:
#         if char == result[-1]:
#             continue
#         result += char
#     return result
#
# text = input()
# print(get_result(text))

# Task 7 String Explosion

# def get_result(word):
#     result = ""
#     explosion = False
#     count = 0
#     for elem in word:
#         if elem == ">":
#             explosion = True
#             result += ">"
#             continue
#         if elem.isdigit() and explosion:
#             explosion = False
#             count += int(elem)
#         if count > 0:
#             count -= 1
#             continue
#         else:
#             result += elem
#     return result
#
# text = input()
# print(get_result(text))

# Task 8 Letters Change Numbers
from string import ascii_lowercase

def get_num(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int("".join(current_num)) * index
                else:
                    result = int("".join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index
    return result

def get_main(lst):
    result = 0

    for num in lst:
        result += get_num(num)

    print(f"{result:.2f}")


text = input().split()
get_main(text)

# Task 9 Rage Quit


# def get_result(word):
#     result = ""
#     container = ""
#     for elem in word:
#         if not elem.isdigit():
#             container += elem.upper()
#             continue
#         if elem.isdigit():
#             container *= int(elem)
#             result += container
#             container = ""
#     symb = set(result)
#     print(f"Unique symbols used {len(symb)}")
#     print(result)
#
# text = input()
# get_result(text)
