"""
Write a program that helps you keep track of your shot targets.
You will receive a sequence with integers,
separated by a single space, representing targets and their value.
Afterward, you will be receiving indices until the "End" command is given,
and you need to print the targets and the count of shot targets.
Every time you receive an index, you need to shoot the target on that index,
if it is possible.
Every time you shoot a target, its value becomes -1,
and it is considered shot. Along with that, you also need to:
·Reduce all the other targets, which have greater values than your current target,
with its value.
·Increase all the other targets, which have less than or equal value
to the shot target, with its value.
Keep in mind that you can't shoot a target, which is already shot.
You also can't increase or reduce a target, which is considered shot.
When you receive the "End" command,
print the targets in their current state and the count of shot targets
in the following format:
"Shot targets: {count} -> {target1} {target2}… {target}"
"""


def get_count(lst, ind):
    target_value = lst[ind]
    for index, target in enumerate(lst):
        if target > target_value:
            lst[index] -= target_value
        elif target == - 1:
            continue
        else:
            lst[index] += target_value
    lst[ind] = -1
    return lst


def get_shoot(lst):
    shot_target = 0
    while True:
        command = input()
        if command == "End":
            message = f"Shot targets {shot_target} ->"
            print(message, *lst, sep=" ")
            break
        target = int(command)
        if target in range(len(lst)):
            shot_target += 1
            lst = get_count(lst, target)


shots = list(map(int, input().split()))
get_shoot(shots)

