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

# Task 5 Office Chairs

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

lst = list(map(int, input().split(", ")))
gr_10 = [num for num in lst if 0 <= num <= 10]
gr_20 = [num for num in lst if 11 <= num <= 20]
gr_30 = [num for num in lst if 21 <= num <= 30]
gr_40 = [num for num in lst if 31 <= num <= 40]
gr_50 = [num for num in lst if 41 <= num <= 50]

print(f"Group of 10's: {gr_10}")
print(f"Group of 20's: {gr_20}")
print(f"Group of 30's: {gr_30}")
print(f"Group of 40's: {gr_40}")
print(f"Group of 50's: {gr_50}")

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


