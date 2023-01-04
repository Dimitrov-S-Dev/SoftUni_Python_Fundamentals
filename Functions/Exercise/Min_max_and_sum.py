def get_min(lst):
    return min(lst)


def get_max(lst):
    return max(lst)


def get_sum(lst):
    return sum(lst)


numbers = list(map(int, input().split()))
print(f"The minimum number is {get_min(numbers)}")
print(f"The maximum number is {get_max(numbers)}")
print(f"The sum number is: {get_sum(numbers)}")
