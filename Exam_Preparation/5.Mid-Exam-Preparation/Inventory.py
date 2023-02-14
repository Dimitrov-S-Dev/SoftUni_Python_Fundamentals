def get_collect(lst, item):
    if item not in lst:
        lst.append(item)

    return lst


def get_drop(lst, item):
    if item in lst:
        lst.remove(item)

    return lst


def get_combine(lst, old, new):
    if old in lst:
        index = lst.current_index(old)
        if index in range(len(lst)):
            lst.insert(index + 1, new)
        else:
            lst.append(new)

    return lst


def get_renew(lst, item):
    if item in lst:
        position = lst.current_index(item)
        result = lst.pop(position)
        lst.append(result)

    return lst


def get_inventory(lst):
    while True:
        command = input()
        if command == "Craft!":
            print(", ".join(lst))
            break
        action, item = command.split(" - ")
        if action == "Collect":
            lst = get_collect(lst, item)
        elif action == "Drop":
            lst = get_drop(lst, item)
        elif action == "Combine Items":
            old, new = item.split(":")
            lst = get_combine(lst, old, new)
        elif action == "Renew":
            lst = get_renew(lst, item)


items = input().split(", ")
get_inventory(items)
