# Task 1 World Tour

# def get_while(string):
#     while True:
#         command = input()
#         if command == "Travel":
#             break
#         info = command.split(":")
#         action = info[0]
#
#         if action == "Add Stop":
#             index = int(info[1])
#             str = info[2]
#             if index in range(len(string)):
#                 string = string[0:index] + str + string[index:]
#             print(string)
#         elif action == "Remove Stop":
#             start_index = int(info[1])
#             end_index = int(info[2])
#             if start_index in range(len(string)) and end_index in range(len(string)):
#                 end_index += 1
#                 string = string[0: start_index] + string[end_index:]
#             print(string)
#
#         elif action == "Switch":
#             old = info[1]
#             new = info[2]
#             if old in string:
#                 string = string.replace(old, new)
#             print(string)
#
#     return string
#
#
# def get_print(string):
#     print(f"Ready for world tour! Planned stops: {string}")
# def get_world_tour(string):
#     string = get_while(string)
#     get_print(string)
#
#
# text = input()
# get_world_tour(text)

# Task 2 Ad Astra
#
# import re
#
# pattern = r"\#([A-Z a-z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|([A-Z a-z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|"
# text = input()
#
# calories = 0
# for_print = []
# matches = re.findall(pattern, text)
# for match in matches:
#     curr_match = [elem for elem in match if elem != ""]
#     calories += int(curr_match[2])
#     for_print.append(curr_match)
#
# days = calories // 2000
# print(f"You have food to last you for: {days} days!")
# for elem in for_print:
#     print(f"Item: {elem[0]}, Best before: {elem[1]}, Nutrition: {elem[2]}")

# Task 3 P!rates

def get_sail():
    pirates_dict = {}
    while True:
        command = input()
        if command == "Sail":
            break
        town, population, gold = command.split("||")
        population = int(population)
        gold = int(gold)
        if town not in pirates_dict.keys():
            pirates_dict[town] = {"population": 0, "gold": 0}
        pirates_dict[town]["population"] += population
        pirates_dict[town]["gold"] += gold

    return  pirates_dict


def get_while(pirates_dict):
    while True:
        command = input()
        if command == "End":
            break

        info = command.split("=>")
        action = info[0]
        town = info[1]

        if action == "Plunder":
            people = int(info[2])
            gold = int(info[3])
            pirates_dict[town]["population"] -= people
            pirates_dict[town]["gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if pirates_dict[town]["population"] == 0 or pirates_dict[town]["gold"] == 0:
                del pirates_dict[town]
                print(f"{town} has been wiped off the map!")
        elif action == "Prosper":
            gold = int(info[2])
            if gold < 0:
                print(f"Gold added cannot be a negative number!")
            else:
                pirates_dict[town]["gold"] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {pirates_dict[town]['gold']} gold.")

    return pirates_dict


def get_print(pirates_dict):
    if len(pirates_dict) > 0:
        print(f"Ahoy, Captain! There are {len(pirates_dict)} wealthy settlements to go to:")
        for town in pirates_dict.keys():
            print(f"{town} -> Population: {pirates_dict[town]['population']} citizens, Gold: {pirates_dict[town]['gold']} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

def get_pirates():
    pirates_dict = get_sail()
    pirates_dict = get_while(pirates_dict)
    get_print(pirates_dict)

get_pirates()
