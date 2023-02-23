# # Task 1 Bakery
#
# items = input().split()
# bakery = {}
#
# for index in range(0, len(items), 2):
#     key = items[index]
#     value = int(items[index + 1])
#     bakery[key] = value
#
# print(bakery)
#
#
# # Task 2 Stock
#
# items = input().split()
# search_products = input().split()
# bakery = {}
#
# for index in range(0, len(items), 2):
#     key = items[index]
#     value = int(items[index + 1])
#     bakery[key] = value
#
# for product in search_products:
#     if product in bakery.keys():
#         quantity = bakery[product]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")

# Task 3 Statistics

# products ={}
#
# while True:
#     command = input()
#     if command == "statistics":
#         break
#     items = command.split(": ")
#     for index in range(0, len(items), 2):
#         key = items[index]
#         value = int(items[index + 1])
#         if key not in products:
#             products[key] = 0
#         products[key] += value
#
#
# print(f"Products is stock:")
# for elem in products:
#     print(f"- {elem}")
# print(f"Total Products: {len(products)}")
# print(f"Total Quantity: {sum(products.values())}")

# Task 4 Students

# students = {}
# command = input().split(":")
#
# while len(command) > 1:
#     name, id_num, course = command[0], command[1], command[2]
#     if course not in students:
#         students[course] = []
#     students[course].append(f"{name} - {id_num}")
#     command = input().split(":")
#
# searched_course = command[0].replace("_", " ")
# for student in students[searched_course]:
#     print(student)

# Task 5 ASCII Value

chars = input().split(", ")

chars_dict = {key:ord(key) for key in chars}
print(chars_dict)