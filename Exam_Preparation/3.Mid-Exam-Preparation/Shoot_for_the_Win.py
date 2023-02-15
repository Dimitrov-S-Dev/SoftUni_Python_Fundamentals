def get_shot(lst, ind):
    target_value = lst[ind]
    lst[ind] = - 1
    for index, value in enumerate(lst):
        if value == - 1:
            continue
        if value > target_value:
            lst[index] -= target_value
        elif value <= target_value:
            lst[index] += target_value
    return lst


def get_main(lst):
    shot_target = 0
    while True:
        command = input()
        if command == "End":
            break
        index = int(command)
        if index in range(len(lst)) and lst[index] != -1:
            lst = get_shot(lst, index)
            shot_target += 1
    result = [str(num) for num in lst]
    return f"Shot targets: {shot_target} -> {' '.join(result)}"


targets = [int(x) for x in input().split()]
print(get_main(targets))
