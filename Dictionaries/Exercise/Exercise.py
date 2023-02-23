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

result = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in result:
        result[course_name] = []
    result[course_name].append(student_name)

for key in result.keys():
    print(f"{key}: {len(result[key])}")
    for el in result[key]:
        print(f"-- {el}")


