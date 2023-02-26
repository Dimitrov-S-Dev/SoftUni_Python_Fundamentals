def get_distribution(lst, num):
    max_num = max(lst)
    max_num_index = lst.current_index(max_num)
    if len(lst) * num > sum(lst):
        return f"No equal distribution possible"
    for index, value in enumerate(lst):
        diff = num - value
        if diff > 0:
            lst[max_num_index] -= diff
            lst[index] += diff
    return lst


numbers = [int(x) for x in input().split(", ")]
min_wealth = int(input())
print(get_distribution(numbers, min_wealth))
