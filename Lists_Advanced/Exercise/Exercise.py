# Task 1 Which Are In?

first = input().split(", ")
second = input().split(", ")
result = []

for w1 in first:
    for w2 in second:
        if w1 in w2 and w1 not in result:
            result.append(w1)

print(result)

# Task 2 Next Version


def get_version(lst):
    version_int = int("".join(lst)) + 1
    version_lst = [num for num in str(version_int)]
    print(".".join(version_lst))


version_str = input().split(".")
get_version(version_str)

# Task 3 Word Filter

text = input().split()
result = [el for el in text if len(el) % 2 == 0]

for word in result:
    print(word)

# Task 4 Number Classification


def get_positive(lst):
    result = [str(el) for el in lst if el >= 0]
    return ", ".join(result)


def get_negative(lst):
    result = [str(el) for el in lst if el < 0]
    return ", ".join(result)


def get_even(lst):
    result = [str(el) for el in lst if el % 2 == 0]
    return ", ".join(result)


def get_odd(lst):
    result = [str(el) for el in lst if el % 2 != 0]
    return ", ".join(result)


numbers = list(map(int, input().split(", ")))

print(f"Positive: {get_positive(numbers)}")
print(f"Negative: {get_negative(numbers)}")
print(f"Even: {get_even(numbers)}")
print(f"Odd: {get_odd(numbers)}")

# Task 5.Mid-Exam-Preparation Office Chairs

count_iter = int(input())
free_chairs = 0
condition = True

for room in range(1, count_iter + 1):
    current_room = input().split()
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    if chairs < visitors:
        diff = visitors - chairs
        print(f"{diff} more chairs needed in room {room}")
        condition = False
    else:
        free_chairs += chairs - visitors

if condition:
    print(f"Game On, {free_chairs} free chairs left")

# Task 6 Electron Distribution


def get_electron(num):
    result = []
    count = 0
    while num:
        count += 1
        position = 2 * count ** 2
        if num > position:
            result.append(position)
            num -= position
        else:
            result.append(num)
            num = 0
    return result


electron = int(input())
print(get_electron(electron))

# Task 7 Group of 10's

"""
from math import ceil

numbers = [int(x) for x in input().split(', ')]
low_boundary = 1
high_boundary = 10
max_number = ceil(max(numbers) / 10)
for idx in range(1, max_number + 1):
    grouped_numbers = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {idx * 10}'s: {grouped_numbers}")
    low_boundary += 10
    high_boundary += 10

"""


# Task 8 Decipher This!

# messages = input().split()
# final_message = []
#
# for message in messages:
#     number = ""
#     current_message = ""
#     for character in message:
#         if character.isdigit():
#             number += character
#         else:
#             break
#     message = message.replace(number, "")
#     number = int(number)
#     current_message += chr(number)
#     if len(message) > 1:
#         message = message[-1] + message[1: - 1] + message[0]
#     current_message += message
#     final_message.append(current_message)
#
# print(" ".join(final_message))

messages = input().split()
decipher_message = []

for message in messages:
    char = [el for el in message if not el.isdigit()]
    digit = [el for el in message if el.isdigit()]
    char_digit = [chr(int("".join(digit)))]
    char[0], char[-1] = char[-1], char[0]
    new_message = char_digit + char
    decipher_message.append("".join(new_message))

print(" ".join(decipher_message))

# Task 9 Moving Target

def get_shoot(lst, idx, power):
    if idx in range(len(lst)):
        if power >= lst[idx]:
            lst.pop(idx)
        else:
            lst[idx] -= power
    return lst


def get_add(lst, idx, val):
    if idx in range(len(lst)):
        lst.insert(idx, val)
    else:
        print("Invalid placement!")
    return lst


def get_strike(lst, idx, val):
    lst.pop(idx + val)
    lst.pop(idx)
    lst.pop(idx - val)
    return lst


def get_main(lst):
    while True:
        command = input()
        if command == "End":
            break
        info = command.split()
        action = info[0]
        index = int(info[1])
        value = int(info[2])

        if action == "Shoot":
            lst = get_shoot(lst, index, value)
        elif action == "Add":
            lst = get_add(lst, index, value)
        elif action == "Strike":
            condition = True
            if index in range(len(lst)):
                if (index + value) in range(len(lst)):
                    if (index - value) in range(len(lst)):
                        condition = False
                        lst = get_strike(lst, index, value)
            if condition:
                print("Strike missed!")
    return lst


target_values = [int(x) for x in input().split()]
print(*get_main(target_values), sep="|")

# Task 10 Heart Delivery

house_number = list(map(int, input().split("@")))
index = 0

while True:
    command = input()
    if command == "Love!":
        break
    info = command.split()
    jump = int(info[1])
    current_index = index + jump

    if current_index >= len(house_number):
        current_index = 0
    if house_number[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        house_number[current_index] -= 2
        if house_number[current_index] == 0:
            print(f"Place {current_index} has a Valentine's day")

    index = current_index

print(f"Cupid's last position was {index}")

mission = [el for el in house_number if el != 0]
if len(mission) > 0:
    print(f"Cupid has failed {len(mission)} places.")
else:
    print(f"Mission was successful.")

# Task 11 Inventory

def collect_func(data, item):
    if item not in data:
        data.append(item)
    return data


def drop_func(data, item):
    if item in data:
        data.remove(item)
    return data


def combine_func(data, items):
    items = items.split(":")
    old_elem = items[0]
    new_elem = items[1]

    if old_elem in data:
        index_old_elem = data.index(old_elem)
        data.insert(index_old_elem + 1, new_elem)

    return data


def renew_func(data, item):
    if item in data:
        data.remove(item)
        data.append(item)
    return data


def get_inventory(data):
    while True:
        command = input().split(" - ")
        if command[0] == "Craft!":
            print(", ".join(data))
            break
        current_command = command[0]
        item = command[1]

        if current_command == "Collect":
            data = collect_func(data, item)
        elif current_command == "Drop":
            data = drop_func(data, item)
        elif current_command == "Combine Items":
            data = combine_func(data, item)
        elif current_command == "Renew":
            data = renew_func(data, item)


info = input().split(", ")
get_inventory(info)

