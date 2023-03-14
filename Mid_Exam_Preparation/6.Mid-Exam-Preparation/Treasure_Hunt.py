def get_loot(lst, *args):
    for item in args:
        if item not in lst:
            lst.insert(0, item)
    return lst


def get_drop(lst, indx):
    a = lst.pop(indx)
    lst.append(a)
    return lst


def get_steal(lst, number):
    stolen_items = []
    while number and lst:
        item = lst.pop()
        stolen_items.append(item)
        number -= 1
    print(stolen_items[:: -1])
    return lst


def get_main(lst):
    while True:
        command = input()
        if command == "Yohoho!":
            break
        action, *items = command.split()

        if action == "Loot":
            lst = get_loot(lst, *items)
        elif action == "Drop":
            index = int(*items)
            lst = get_drop(lst, index)
        elif action == "Steal":
            count = int(*items)
            lst = get_steal(lst, count)
    lenght = 0
    for el in lst:
        lenght += len(el)
    try:
        avg_treasure = lenght / len(lst)
        return f"Average treasure gain: {avg_treasure:.2f} pirate credit."
    except:
        return f"Failed treasure hunt."


treasure_chest = input().split("|")
print(get_main(treasure_chest))



