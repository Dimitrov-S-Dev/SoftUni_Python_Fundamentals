def get_inset(lst, i, num):
    lst[i] += num
    return lst


def get_leave(lst, i, num):
    lst[i] -= num
    return lst


wagons_count = int(input())
train = [0] * wagons_count

command = input()

while command != 'End':
    info = command.split()
    action = info[0]
    if action == 'add':
        train[-1] += int(info[1])

    elif action == 'insert':
        index = int(info[1])
        people = int(info[2])
        get_inset(train, index, people)

    elif action == 'leave':
        index = int(info[1])
        people = int(info[2])
        get_leave(train, index, people)
    command = input()

print(train)
