# Task 1 World Tour

def get_add(string, i, element):
    if i in range(len(string)):
        string = string[0:i] + element + string[i:]
    return string

def get_remove(string, start_i, end_i):
    if start_i in range(len(string)) and end_i in range(len(string)):
        string = string[0:start_i] + string[end_i + 1:]
    return string

def get_switch(string, old, new):
    if old in string:
        string = string.replace(old, new)
    return string


def get_word_tour(text):
    while True:
        command = input()
        if command == "Travel":
            break
        info = command.split(":")
        action = info[0]

        if action == "Add Stop":
            index = int(info[1])
            word = info[2]
            text = get_add(text, index, word)
        elif action == "Remove Stop":
            start_index = int(info[1])
            end_index = int(info[2])
            text = get_remove(text, start_index, end_index)
        elif action == "Switch":
            old_str = info[1]
            new_str = info[2]
            text = get_switch(text, old_str, new_str)
        print(text)

    print(f"Ready for world tour! Planned stops: {text}")

data = input()
get_word_tour(data)


# Task 2 Mirror Words

import re

pattern = r"(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
text = input()
pairs = []
flag = 0
matches = re.findall(pattern, text)
if matches:
    flag = 1
    for match in matches:
        if match[1] == match[-1][::-1]:
            pairs.append(f"{match[1]} <=> {match[-1]}")

else:
    print(f"No word pairs found!")
if flag:
    if pairs:
        print(f"{len(matches)} word pairs found!")
        print(f"The mirror words are:")
        for elem in pairs:
            print(elem)

    else:
        print(f"No mirror words!")

# Task 3 Heroes of Code and Logic VII

def get_info(num):
    heroes_dict = {}
    for _ in range(num):
        hero_name, hp_points, mp_points = input().split()
        hp_points = int(hp_points)
        mp_points = int(mp_points)
        heroes_dict[hero_name] = [hp_points, mp_points]

    return heroes_dict


def get_spell(dict, name, mp_points, spell):
    if dict[name][1] >= mp_points:
        points_left = dict[name][1] - mp_points
        dict[name][1] = points_left
        print(f"{name} has successfully cast {spell} and now has {points_left} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")

    return dict

def get_damage(dict, name, mp_points, attacker):
    current_hp = dict[name][0] - mp_points
    if current_hp > 0:
        dict[name][0] -= mp_points
        print(f"{name} was hit for {mp_points} HP by {attacker} and now has {current_hp} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del dict[name]

    return dict


def get_charge(dict, name, amount):
    current_mp = dict[name][1]
    if current_mp + amount > 200:
        dict[name][1] = 200
    else:
        dict[name][1] = current_mp + amount
    diff = abs(current_mp - dict[name][1])
    print(f"{name} recharged for {diff} MP!")
    return dict
def get_heal(dict, name, points):
    current_hp_points = dict[name][0]
    if current_hp_points + points > 100:
        dict[name][0] = 100
    else:
        dict[name][0] += points
    diff = abs(current_hp_points - dict[name][0])
    print(f"{name} healed for {diff} HP!")
    return dict
def get_heroes(number):
    heroes_dict = get_info(number)
    while True:
        command = input()
        if command == "End":
            break
        info = command.split(" - ")
        action = info[0]
        name = info[1]

        if action == "CastSpell":
            mp_points = int(info[2])
            spell = info[3]
            heroes_dict = get_spell(heroes_dict,name, mp_points, spell)

        elif action == "TakeDamage":
            damage = int(info[2])
            attacker = info[3]
            heroes_dict = get_damage(heroes_dict, name, damage, attacker)

        elif action == "Recharge":
            amount = int(info[2])
            heroes_dict = get_charge(heroes_dict, name, amount)

        elif action == "Heal":
            hp_points = int(info[2])
            heroes_dict = get_heal(heroes_dict, name, hp_points)
    for key, value in heroes_dict.items():
        print(f"{key}")
        print(f"HP: {value[0]}")
        print(f"MP: {value[1]}")


n = int(input())
get_heroes(n)

