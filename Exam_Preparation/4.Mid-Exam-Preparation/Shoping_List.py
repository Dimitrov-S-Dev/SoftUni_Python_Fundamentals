def get_urgent(lst, el):
    if el not in lst:
        lst.insert(0, el)
    return lst


def get_unnecessary(lst, el):
    if el in lst:
        lst.remove(el)
    return lst


def get_correct(lst, old, new_el):
    if old in lst:
        position = lst.index(old)
        lst[position] = new_el
    return lst


def get_rearrange(lst, el):
    if el in lst:
        index = lst.index(el)
        item = lst.pop(index)
        lst.append(item)
    return lst


def get_main(lst):
    while True:
        command = input()
        if command.startswith("Go"):
            print(", ".join(lst))
            break
        info = command.split()
        action = info[0]
        element = info[1]

        if action == "Urgent":
            lst = get_urgent(lst, element)
        elif action == "Unnecessary":
            lst = get_unnecessary(lst, element)
        elif action == "Correct":
            new_element = info[2]
            lst = get_correct(lst, element, new_element)
        elif action == "Rearrange":
            lst = get_rearrange(lst, element)


grocery_list = [x for x in input().split("!")]
get_main(grocery_list)


