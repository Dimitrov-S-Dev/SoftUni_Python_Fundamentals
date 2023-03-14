# Task 1 Secret Chat

def get_insert(word, i):
    word = word[0:i] + " " + word[i:]
    return word

def get_reverse(word, sub_word):
    if sub_word in word:
        word = word.replace(sub_word,sub_word[::-1])
    else:
        print("error")
    return word


def get_change(word, search_elem, replace_elem):
    new_word = ""
    for elem in word:
        if elem == search_elem:
            new_word += replace_elem
        else:
            new_word += elem
    return new_word


def get_secret_char(message):
    while True:
        command = input()
        if command == "Reveal":
            break
        info = command.split(":|:")
        action = info[0]

        if action == "InsertSpace":
            index = int(info[1])
            message = get_insert(message, index)
        elif action == "Reverse":
            substring = info[1]
            message = get_reverse(message, substring)
        elif action == "ChangeAll":
            substring = info[1]
            replacement = info[2]
            message = get_change(message, substring, replacement)

    print(f"You have a new message message: {message}")


data = input()
get_secret_char(data)

# Task 2 Destination Mapper

import re

pattern = r"(?P<sep>[=\/])?(?P<dest>[A-Z][]a-z]+)\1"
text = input()
destinations = []
travel_points = 0

matches = re.finditer(pattern, text)
for match in matches:
    destinations.append(match.group("dest"))
    travel_points += len(match.group("dest"))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")

# Task 3 The Pianist

def get_data(num):
    pianist_dict = {}
    for _ in range(num):
        piece, composer, key = input().split("|")
        pianist_dict[piece] = [composer, key]
    return pianist_dict

def get_add(dict,piece, key , composer):
    if piece not in dict.keys():
        dict[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return dict

def get_remove(dict, piece):
    if piece in dict.keys():
        del dict[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return  dict


def get_change(dict, piece, key):
    if piece in dict.keys():
        dict[piece][1] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return dict


def get_pianist(number):
    pianist_dict = get_data(number)

    while True:
        command = input()
        if command == "Stop":
            break
        info = command.split("|")
        action = info[0]
        if action == "Add":
            piece = info[1]
            composer = info[2]
            key = info[3]
            pianist_dict = get_add(pianist_dict, piece, key, composer)
        elif action == "Remove":
            piece = info[1]
            pianist_dict = get_remove(pianist_dict, piece)
        elif action == "ChangeKey":
            piece = info[1]
            new_key = info[2]
            pianist_dict = get_change(pianist_dict, piece, new_key)
    for key, value in sorted(pianist_dict.items()):
        print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

num_pieces = int(input())
get_pianist(num_pieces)
