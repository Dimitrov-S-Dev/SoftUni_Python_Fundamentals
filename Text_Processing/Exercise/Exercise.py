# Task 1 Valid Usernames
# import string
#
# def get_main(lst):
#     flag = 0
#     expected_element = string.digits + string.ascii_letters + "-" + "_"
#     for name in lst:
#         flag = 0
#         if 3 > len(name) or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_element]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)
#
# username = input().split(", ")
# get_main(username)

# Task 2 Character Multiplier