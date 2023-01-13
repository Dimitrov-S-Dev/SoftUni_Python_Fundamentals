"""
Input / Constraints
You will receive a journal with some collecting items,
separated with a comma and a space (", ").
After that, until receiving "Craft!" you will be receiving different
commands split by " - ":
· "Collect - {item}" - you should add the given item to your inventory.
If the item already exists, you should skip this line.
· "Drop - {item}" - you should remove the item from your inventory
if it exists.
· "Combine Items - {old_item}:{new_item}" -
you should check if the old item exists.
If so, add the new item after the old one.
Otherwise, ignore the command.
· "Renew – {item}" – if the given item exists,
you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory,
separated by ", ".
"""


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
        index = lst.index(old)
        if index in range(len(lst)):
            lst.insert(index + 1, new)
        else:
            lst.append(new)

    return lst


def get_renew(lst, item):
    if item in lst:
        position = lst.index(item)
        result = lst.pop(position)
        lst.append(result)

    return lst


def get_inventory(lst):
    while True:
        command = input().split(" - ")
        action = command[0]
        if action == "Craft!":
            print(", ".join(lst))
            break
        item = command[1]
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
