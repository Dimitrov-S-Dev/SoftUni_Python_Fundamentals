"""
You will receive a journal with some Collecting items,
separated with ", " (comma and space).
After that, until receiving "Craft!"
you will be receiving different commands.
Commands (split by " - "):
· "Collect - {item}" – Receiving this command,
you should add the given item to your inventory.
If the item already exists, you should skip this line.
· "Drop - {item}" – You should remove the item from your inventory
if it exists.
· "Combine Items - {oldItem}:{newItem}"
You should check if the old item exists.
If so, add the new item after the old one. Otherwise, ignore the command.
· "Renew – {item}" – If the given item exists,
you should change its position and put it last in your inventory.
"""


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
