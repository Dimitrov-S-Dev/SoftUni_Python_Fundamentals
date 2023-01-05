def get_inset(lst, i, num):
    lst[i] += num
    return lst


def get_leave(lst, i, num):
    lst[i] -= num
    return lst


wagons_count = int(input())
wagons_lst = [0] * wagons_count

command = input()

while command != 'End':
    info = command.split()
    action = info[0]
    if action == 'add':
        wagons_lst[-1] += int(info[1])

    elif action == 'insert':
        index = int(info[1])
        people = int(info[2])
        get_inset(wagons_lst, index, people)

    elif action == 'leave':
        index = int(info[1])
        people = int(info[2])
        get_leave(wagons_lst, index, people)
    command = input()

print(wagons_lst)
