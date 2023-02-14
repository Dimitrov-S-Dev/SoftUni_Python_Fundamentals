def get_urgent(lst, el):
    if el not in lst:
        lst.insert(0, el)
    return lst


def get_unnecessary(lst, el):
    if el in lst:
        lst.remove(el)
    return lst


def get_correct(lst, el, new_el):
    if el in lst:
        lst[el] = new_el
    return lst


def get_rearrange(lst, el):
    if el in lst:
        position = lst.current_index(el)
        item = lst.pop(position)
        lst.append(item)
    return lst


def get_main(lst):
    while True:
        command = input()
        if command == "Go Shopping!":
            break
        info = command.split()
        action = info[0]
        item = info[1]

        if action == "Urgent":
            lst = get_urgent(lst, item)
        elif action == "Unnecessary":
            lst = get_unnecessary(lst, item)
        elif action == "Correct":
            new_item = info[2]
            lst = get_correct(lst, item, new_item)
        elif action == "Rearrange":
            lst = get_rearrange(lst, item)
    return lst


grocery_list = input().split("!")
print(", ".join(get_main(grocery_list)))

