"""
Write a program that finds a place for the tourist on a lift.
Every wagon should have a maximum of 4 people on it.
If a wagon is full, you should direct the people to the next one
with space available.
"""


def get_on_lift(lst, people):
    new_lst = []
    for index, value in enumerate(lst):
        if value > 0:
            capacity = 4 - value
        else:
            capacity = 4

        if capacity < people:
            new_lst.append(str(4))
        else:
            new_lst.append(str(people))
        people -= capacity

    if people > 0:
        return f"There isn't enough space! {people} people in a queue!\n{' '.join(new_lst)}"
    else:
        return f"The lift has empty spots!\n{' '.join(new_lst)}"


people_waiting = int(input())
lift = list(map(int, input().split()))
print(get_on_lift(lift, people_waiting))
