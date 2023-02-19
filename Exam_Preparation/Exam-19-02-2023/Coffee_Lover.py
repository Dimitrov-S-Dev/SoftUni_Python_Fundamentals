def get_include(lst, el):
    lst.append(el)
    return lst


def get_remove(lst, comm, num):
    if len(lst) >= num:
        if comm == "last":
            for count in range(num):
                lst.pop()
        elif comm == "first":
            lst = lst[num::]
    return lst


def get_prefer(lst, ind1, ind2):
    if ind1 in range(len(lst)) and ind2 in range(len(lst)):
        lst[ind1], lst[ind2] = lst[ind2], lst[ind1]
    return lst


def get_reverse(lst):
    return lst[::-1]


def get_main(lst, counter):
    for count in range(counter):
        current_command = input().split()
        action = current_command[0]
        if action == "Include":
            element = current_command[1]
            lst = get_include(lst, element)
        elif action == "Remove":
            command = current_command[1]
            number = int(current_command[2])
            lst = get_remove(lst, command, number)
        elif action == "Prefer":
            index_one = int(current_command[1])
            index_two = int(current_command[2])
            lst = get_prefer(lst, index_one, index_two)
        elif action == "Reverse":
            lst = get_reverse(lst)
    print(" ".join(lst))


coffees = input().split()
n = int(input())
print("Coffees:")
get_main(coffees, n)

