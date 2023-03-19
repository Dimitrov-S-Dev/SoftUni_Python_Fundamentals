# Task 1 The Limitation Game

# def get_while(string):
#     while True:
#         command = input()
#         if command == "Decode":
#             break
#         info = command.split("|")
#         action = info[0]
#
#         if action == "Move":
#             num_letters = int(info[1])
#             string = string[num_letters:] + string[0:num_letters]
#         elif action == "Insert":
#             index = int(info[1])
#             value = info[2]
#             string = string[0:index] + value + string[index:]
#         elif action == "ChangeAll":
#             substring = info[1]
#             replacement = info[2]
#             string = string.replace(substring, replacement)
#     return string
#
#
# def get_print(string):
#     print(f"The decrypted message is: {string}")
#
# def get_limit_game(string):
#     string = get_while(string)
#     get_print(string)
#
#
# text = input()
# get_limit_game(text)
#

# Task 2 Destination Mapper

# import re
#
# pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
# text = input()
# destinations = []
#
# matches = re.finditer(pattern, text)
# for match in matches:
#     destinations.append(match.group(2))
#
# print(f"Destinations: {', '.join(destinations)}")
# length = 0
# for elem in destinations:
#     length += len(elem)
# print(f"Travel Points: {length}")

# Task 3 Heroes of Code and Logic VII

def get_heroes(number):
    heroes_dict = {}
    for _ in range(number):
        hero_name, hp, mp = input().split()
        hp = int(hp)
        mp = int(mp)
        if hero_name not in heroes_dict.keys():
            heroes_dict[hero_name] = {"hit_points": 0, "mana_points": 0}
        heroes_dict[hero_name]["hit_points"] += hp
        heroes_dict[hero_name]["mana_points"] += mp

    return heroes_dict


def get_while(heroes_dict):
    while True:
        command = input()
        if command == "End":
            break
        info = command.split(" - ")
        action = info[0]
        hero_name = info[1]

        if action == "CastSpell":
            mp_needed = int(info[2])
            spell_name = info[3]

            if heroes_dict[hero_name]["mana_points"] >= mp_needed:
                heroes_dict[hero_name]["mana_points"] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mana_points']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif action == "TakeDamage":
            damage = int(info[2])
            attacker = info[3]
            heroes_dict[hero_name]["hit_points"] -= damage

            if heroes_dict[hero_name]["hit_points"] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['hit_points']} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del heroes_dict[hero_name]

        elif action == "Recharge":
            amount = int(info[2])
            current_mp = heroes_dict[hero_name]["mana_points"]
            if heroes_dict[hero_name]["mana_points"] + amount > 200:
                heroes_dict[hero_name]["mana_points"] = 200

            else:
                heroes_dict[hero_name]["mana_points"] += amount
            diff = heroes_dict[hero_name]["mana_points"] - current_mp
            print(f"{hero_name} recharged for {diff} MP!")

        elif action == "Heal":
            amount = int(info[2])
            current_hp = heroes_dict[hero_name]["hit_points"]
            if heroes_dict[hero_name]["hit_points"] + amount > 100:
                heroes_dict[hero_name]["hit_points"] = 100

            else:
                heroes_dict[hero_name]["hit_points"] += amount
            diff = heroes_dict[hero_name]["hit_points"] - current_hp
            print(f"{hero_name} healed for {diff} HP!")

    return heroes_dict

def get_print(heroes_dict):
    for name in heroes_dict.keys():
        print(f"{name}")
        print(f"HP: {heroes_dict[name]['hit_points']}")
        print(f"MP: {heroes_dict[name]['mana_points']}")


def get_heroes_of_code(number):
    heroes_dict = get_heroes(number)
    heroes_dict = get_while(heroes_dict)
    get_print(heroes_dict)

n = int(input())
get_heroes_of_code(n)

