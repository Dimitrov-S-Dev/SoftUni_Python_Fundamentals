# Task 1 Count Chars in a String

# words_list = input().split()
# word = "".join(words_list)
# result = {}
#
# for char in word:
#     if char not in result.keys():
#         result[char] = 0
#     result[char] += 1
#
# for key, value in result.items():
#     print(f"{key} -> {value}")

# Task 2 A Miner Task

# result = {}
#
# while True:
#     element = input()
#     if element == "stop":
#         break
#     value = int(input())
#     if element not in result.keys():
#         result[element] = 0
#     result[element] += value
#
#
# for key, value in result.items():
#     print(f"{key} -> {value}")

# Task 3 Capitals

# countries = input().split(", ")
# capitals = input().split(", ")
#
# result = {countries[index]: capitals[index] for index in range(len(countries))}
#
# for key, value in result.items():
#     print(f"{key} -> {value}")

# Task 4 Phonebook

# info = input()
# result = {}
#
# while not info.isdigit():
#     name, number = info.split("-")
#     result[name] = number
#     info = input()
#
# count = int(info)
# for _ in range(count):
#     current_name = input()
#     for key, value in result.items():
#         if current_name in key:
#             print(f"{key} -> {value}")
#         else:
#             print(f"Contact {current_name} does not exist.")

# Task 5 Legendary Farming

# result = {"shards": 0, "fragments": 0, "motes": 0}
# info = input().split()
# is_collected = True
#
# while is_collected:
#     for index in range(0, len(info), 2):
#         material = info[index + 1].lower()
#         quantity = int(info[index])
#         if material not in result.keys():
#             result[material] = 0
#         result[material] += quantity
#         if result["shards"] >= 250:
#             result["shards"] -= 250
#             print("Shadowmourne obtained!")
#             is_collected = False
#             break
#         elif result["fragments"] >= 250:
#             result["fragments"] -= 250
#             print("Valanyr obtained!")
#             is_collected = False
#         elif result["motes"] >= 250:
#             result["motes"] -= 250
#             print("Dragonwrath obtained!")
#             is_collected = False
#         if not is_collected:
#             break
#     if not is_collected:
#         break
#     info = input().split()
#
# for key, value in result.items():
#     print(f"{key}: {value}")

# Task 6 Orders

# result = {}
#
# while True:
#     command = input()
#     if command == "buy":
#         break
#     info = command.split()
#     product = info[0]
#     price = float(info[1])
#     quantity = int(info[2])
#     if product not in result:
#         result[product] = 0
#     else:
#         result[price] = price
#     result[product] += quantity * price
#
# for key, value in result.items():
#     print(f"{key} -> {value:.2f}")
#

# Task 7 SoftUni Parking

# count_iter = int(input())
# result = {}
#
# for _ in range(count_iter):
#     info = input().split()
#     action = info[0]
#     if action == "register":
#         name = info[1]
#         number = info[2]
#         if name in result.keys():
#             print(f"ERROR: already registered with plate number {number}")
#         else:
#             result[name] = number
#             print(f"{name} registered {number} successfully")
#     elif action == "unregister":
#         name = info[1]
#         if name in result.keys():
#             print(f"{name} unregistered successfully")
#             del result[name]
#
#         else:
#             print(f"ERROR: user {name} not found")
#
# for key, value in result.items():
#     print(f"{key} => {value}")


# Task 8 Courses

# result = {}
#
# while True:
#     command = input()
#     if command == "end":
#         break
#     course_name, student_name = command.split(" : ")
#     if course_name not in result:
#         result[course_name] = []
#     result[course_name].append(student_name)
#
# for key in result.keys():
#     print(f"{key}: {len(result[key])}")
#     for el in result[key]:
#         print(f"-- {el}")
#

# Task 9 Student Academy

# count_iter = int(input())
# result = {}
#
# for _ in range(count_iter):
#     student = input()
#     grade = float(input())
#     if student not in result.keys():
#         result[student] = []
#     result[student].append(grade)
#
# for key, value in result.items():
#     avg = sum(value) / len(value)
#     if avg >= 4.50:
#         print(f"{key} -> {avg}")

# Task 10 Company Users

# result = {}
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     company_name, employee = command.split(" -> ")
#     if company_name not in result.keys():
#         result[company_name] = []
#     if employee not in result[company_name]:
#         result[company_name].append(employee)
#
# for key in result.keys():
#     print(f"{key}")
#     for el in result[key]:
#         print(f"-- {el}")

# Task 11 Force Book
#
# result = {}
#
# while True:
#     command = input()
#     if command == "exam finished":
#         break
#     info = command.split("-")
#     username = info[0]
#     language = info[1]
#     points = int(info[2])
#     if username not in result:
#         result[username] = {}
#         result[username][language] = []
#     result[username][language].append(points)
#
# print(f"Results:")
#
# print(f"Submissions:")
#

# Task 11 Force Book
# def get_pipe(force, user, info_dict):
#     if force not in info_dict.keys() and user not in info_dict.values():
#         info_dict[force] = []
#         info_dict[force].append(user)
#     condition = True
#     for names in info_dict.values():
#         if user in names:
#             condition = False
#     if condition:
#         info_dict[force].append(user)
#     return info_dict
# def get_arrow(force, user, info_dict):
#     condtion = True
#     for key,value in info_dict.items():
#         if user in value:
#             condtion = False
#             info_dict[key].remove(user)
#     if condtion:
#         if force not in info_dict.keys():
#             info_dict[force] = []
#         info_dict[force].append(user)
#         print(f"{user} joins the {force} side!")
#     else:
#         if force == "Lighter":
#             info_dict["Lighter"].append(user)
#         else:
#             info_dict["Darker"].append(user)
#
#     return info_dict
#
#
# def get_main():
#     user_info = {}
#     while True:
#         command = input()
#         if command == "Lumpawaroo":
#             break
#
#         if "|" in command:
#             info = command.split(" | ")
#             force = info[0]
#             user = info[1]
#             user_info = get_pipe(force, user, user_info)
#         elif "->" in command:
#             info = command.split(" -> ")
#             force = info[1]
#             user = info[0]
#             user_info = get_arrow(force, user, user_info)
#     return user_info
#
# for key, value in get_main().items():
#     print(f"Side: {key}, Members: {len(value)} ! {'! '.join(value)}")
#

