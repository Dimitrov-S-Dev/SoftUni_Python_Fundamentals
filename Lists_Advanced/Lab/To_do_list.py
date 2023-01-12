"""
You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted
by importance in ascending order.
The importance value will always be an integer between
1 and 10 (inclusive).
"""

# command = input()
# importance_lst = [0] * 10
#
# while command != 'End':
#     ind, note = command.split('-')
#     index = int(ind) - 1
#     importance_lst[index] = note
#     command = input()
#
# print([x for x in importance_lst if x != 0])
command = input()
tasks_lst = []

while command != 'End':
    priority, note = command.split('-')
    priority = int(priority)
    tasks_lst.append((priority, note))
    command = input()

result = [x[1] for x in sorted(tasks_lst)]
print(result)
