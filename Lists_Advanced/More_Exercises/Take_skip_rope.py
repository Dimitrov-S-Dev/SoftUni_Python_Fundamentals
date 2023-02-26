def get_char(lst):
    return [el for el in lst if not el.isdigit()]


def get_numbers(lst):
    return [int(el) for el in lst if el.isdigit()]


def get_even(lst):
    even = []
    for index, value in enumerate(lst):
        if index % 2 == 0:
            even.append(value)
    return even


def get_odd(lst):
    odd = []
    for index, value in enumerate(lst):
        if index % 2 != 0:
            odd.append(value)
    return odd


def get_result(lst):
    message = ""
    characters = get_char(lst)
    numbers = get_numbers(lst)
    take_list = get_even(numbers)
    skip_list = get_odd(numbers)

    while take_list:
        char_to_take = take_list.pop(0)
        if char_to_take == 0:
            message += ""
            skip = skip_list.pop(0)
            characters = characters[skip:]
        else:
            skip = skip_list.pop(0)
            message += "".join(characters[:char_to_take])
            characters = characters[char_to_take + skip:]
    return message


text = list(input())

print(get_result(text))
