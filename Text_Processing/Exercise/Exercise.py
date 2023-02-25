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



