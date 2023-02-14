"""
On the first line, you will be given the population
(numbers separated by comma and space ", ").
On the second line, you will be given the minimum wealth.
You should distribute the wealth so that no part
of the population has less than the minimum wealth.
To do that, you should always take wealth from
the wealthiest part of the population.
There will be cases where the distribution
will not be possible.
In that case, print: "No equal distribution possible".
"""


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


numbers = list(map(int, input().split(", ")))
min_wealth = int(input())
print(get_distribution(numbers, min_wealth))
