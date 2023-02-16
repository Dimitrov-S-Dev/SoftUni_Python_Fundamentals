def get_shoot(lst, ind, power):
    if lst[ind] - power <= 0:
        lst.pop(ind)
    else:
        lst[ind] -= power

    return lst


def get_add(lst, ind, value):
    lst.insert(ind, value)

    return lst


def get_strike(lst, ind, radius):
    lst.pop(ind + radius)
    lst.pop(ind)
    lst.pop(ind - radius)

    return lst


def get_main(lst):
    while True:
        command = input()
        if len(command) == 3:
            result = [str(el) for el in lst]
            print("|".join(result))
            break
        action, index, value = command.split()
        index = int(index)
        value = int(value)

        if action == "Shoot":
            if index in range(len(lst)):
                lst = get_shoot(lst, index, value)
        elif action == "Add":
            if index in range(len(lst)):
                lst = get_add(lst, index, value)
            else:
                print("Invalid placement!")
        elif action == "Strike":
            top = index + value
            bottom = index - value
            if bottom >= 0 and index in range(len(lst)) and top < len(lst):
                lst = get_strike(lst, index, value)
            else:
                print("Strike missed!")


targets = [int(x) for x in input().split()]
get_main(targets)
