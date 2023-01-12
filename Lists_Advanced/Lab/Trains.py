"""
You will receive a number representing the number of wagons a train has.
Create a list (train) with the given length containing only zeros.
Until you receive the command "End", you will receive some of the following commands:
•	"add {people}" – you should add the number of people in the last wagon
•	"insert {index} {people}" - you should add the number of people at the given wagon
•	"leave {index} {people}" - you should remove the number of people from the wagon.
There will be no case in which the people will be more than the count in the wagon.
There will be no case in which the index is invalid!
After you receive the "End" command print the train.
"""


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
