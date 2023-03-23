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

# Task 3 P!rates

def get_info():
    pirates_dict = {}
    while True:
        text = input()
        if text == "Sail":
            break
        town, population, gold = text.split("||")
        population = int(population)
        gold = int(gold)
        if town not in pirates_dict.keys():
            pirates_dict[town] = {"population": 0, "gold": 0}
        pirates_dict[town]["population"] += population
        pirates_dict[town]["gold"] += gold

    return pirates_dict


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
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            pirates_dict[town]["population"] -= people
            pirates_dict[town]["gold"] -= gold

            if pirates_dict[town]["population"] == 0 or pirates_dict[town]["gold"] == 0:
                print(f"{town} has been wiped off the map!")
                del pirates_dict[town]


        elif action == "Prosper":
            gold_added = int(info[2])
            if gold_added < 0:
                print(f"Gold added cannot be a negative number!")
            else:
                pirates_dict[town]["gold"] += gold_added
                print(f"{gold_added} gold added to the city treasury. {town} now has {pirates_dict[town]['gold']} gold.")


    return pirates_dict


def get_print(p_dict):
    if p_dict:
        print(f"Ahoy, Captain! There are {len(p_dict)} wealthy settlements to go to:")
        for town in p_dict.keys():
            print(f"{town} -> Population: {p_dict[town]['population']} citizens, Gold: {p_dict[town]['gold']} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

def get_pirates():
    pirates_dict = get_info()
    pirates_dict = get_while(pirates_dict)
    get_print(pirates_dict)


get_pirates()

