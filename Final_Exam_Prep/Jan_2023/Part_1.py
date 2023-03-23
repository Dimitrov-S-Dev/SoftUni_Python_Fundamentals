# Task 1 The Limitation Game

# def get_while(message):
#     while True:
#         command = input()
#         if command == "Decode":
#             break
#         info = command.split("|")
#         action = info[0]
#
#         if action == "Move":
#             num_letters = int(info[1])
#             message = message[num_letters:] + message[0:num_letters]
#
#         elif action == "Insert":
#             index = int(info[1])
#             value = info[2]
#             message = message[0:index] + value + message[index:]
#
#         elif action == "ChangeAll":
#             substring = info[1]
#             replacement = info[2]
#             message = message.replace(substring, replacement)
#
#     return message
#
#
# def get_print(message):
#     print(f"The decrypted message is: {message}")
#
#
# def get_limitation(message):
#     message = get_while(message)
#     get_print(message)
#
#
#
# data = input()
# get_limitation(data)

# Task 2 Fancy Barcodes

# import re
#
# n = int(input())
#
# for _ in range(n):
#     barcode = input()
#     pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z]{1})(@#+)"
#     matches = re.search(pattern, barcode)
#     product_group = ""
#     if matches:
#         for elem in matches.group(2):
#             if elem.isdigit():
#                 product_group += elem
#         if product_group:
#             print(f"Product group: {product_group}")
#         else:
#             print(f"Product group: 00")
#     else:
#         print(f"Invalid barcode")


