def get_swap(lst, ind1, ind2):
    lst[ind1], lst[ind2] = lst[ind2], lst[ind1]
    return lst


def get_multiply(lst, ind1, ind2):
    lst[ind1] = lst[ind1] * lst[ind2]
    return lst


def get_decrease(lst):
    return [(x - 1) for x in lst]


def get_main(lst):
    while True:
        command = input()
        if command == "end":
            return lst
        info = command.split()
        action = info[0]
        if action == "swap":
            index1 = int(info[1])
            index2 = int(info[2])
            lst = get_swap(lst, index1, index2)
        elif action == "multiply":
            index1 = int(info[1])
            index2 = int(info[2])
            lst = get_multiply(lst, index1, index2)
        elif action == "decrease":
            lst = get_decrease(lst)


numbers = [int(x) for x in input().split()]
print(*get_main(numbers), sep=", ")
