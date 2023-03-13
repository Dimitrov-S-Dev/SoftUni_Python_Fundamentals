# Task 1 Valid Usernames

import string

def get_main(lst):
    expected_element = string.digits + string.ascii_letters + "-" + "_"
    for name in lst:
        condition = True
        if 3 > len(name) or len(name) > 16:
            condition = False
        elif len([x for x in name if x in expected_element]) != len(name):
            condition = False
        elif condition:
            print(name)

username = input().split(", ")
get_main(username)



# Task 2 Character Multiplier

def get_result(first, second):
    total_sum = 0
    for i in range(len(first)):
        if i < len(second):
            total_sum += ord(first[i]) * ord(second[i])
        else:
            total_sum += ord(first[i])
    return total_sum

def get_multiply(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = get_result(first_word, second_word)
    else:
        result = get_result(second_word, first_word)
    print(result)


data = input().split()
get_multiply(data[0],data[1])

# Task 3 Extract File

def get_name(word):
    name, extension = word.split(".")
    result = f"File name: {name}"
    result += f"\nFile extension: {extension}"
    return result

file = input().split("\\")
print(get_name(file[-1]))

# Task 4 Caesar Cipher

text = input()
result = ""

for char in text:
    index = ord(char) + 3
    result += chr(index)

print(result)

# Task 5 Emoticon Finder

text = input("")

for index in range(len(text)):
    if text[index] == ":":
        print(f"{text[index]}{text[index + 1]}")

# Task 6  Replace Repeating Chars

def get_result(word):
    result = word[0]
    for char in word:
        if char == result[-1]:
            continue
        result += char
    return result

text = input()
print(get_result(text))

# Task 7 String Explosion

def get_result(word):
    result = ""
    explosion = False
    count = 0
    for elem in word:
        if elem == ">":
            explosion = True
            result += ">"
            continue
        if elem.isdigit() and explosion:
            explosion = False
            count += int(elem)
        if count > 0:
            count -= 1
            continue
        else:
            result += elem
    return result

text = input()
print(get_result(text))

# Task 8 Letters Change Numbers

from string import ascii_lowercase

def get_num(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int("".join(current_num)) * index
                else:
                    result = int("".join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index
    return result

def get_main(lst):
    result = 0

    for num in lst:
        result += get_num(num)

    print(f"{result:.2f}")


text = input().split()
get_main(text)

# Task 9 Rage Quit

text = input().upper()

result = ""
container = ""

for i in range(len(text)):
    if not text[i].isdigit():
        container += text[i]
    else:
        num = text[i]
        if i + 1 in range(len(text)):
            if text[i + 1].isdigit():
                num += text[i + 1]
        container *= int(num)
        result += container
        container = ""

symb = set(result)
print(f"Unique symbols used: {len(symb)}")
print(result)


# Task 10 Winning Ticket

def additional_func(partition):
    curr_max_sum = 0
    special_char = ""

    for char in partition:
        if char != special_char:
            if curr_max_sum >= 6:
                break
            curr_max_sum = 1
            special_char = char
        else:
            curr_max_sum += 1
    return [curr_max_sum, special_char]

def ticket_validator(text):
    ticket_condition = ""
    if len(text) != 20:
        ticket_condition = "invalid ticket"
    elif text[0] * 20 == text and text[0] in "@#$^":
        ticket_condition = f'ticket "{text}" - 10{text[0]} Jackpot!'
    else:
        data_source = ""
        if additional_func(text[0:int(len(text) / 2)]) > additional_func(text[int(len(text) / 2):]):
            data_source = additional_func(text[int(len(text) / 2):])
        else:
            data_source = additional_func(text[0:int(len(text) / 2)])
        number_of_spec_signs = data_source[0]
        special_char = data_source[1]

        if number_of_spec_signs < 6 or special_char not in "@#^$":
            ticket_condition = f'ticket "{text}" - no match'
        else:
            ticket_condition = f'ticket "{text}" - {number_of_spec_signs}{special_char} '
    return ticket_condition

def get_winning_ticket(lst):
    for ticket in lst:
        print(ticket_validator(ticket))

tickets = input()
data = [x.strip() for x in tickets.split(", ")]
get_winning_ticket(data)
