def get_cheap(lst, ind):
    sum_left = 0
    sum_right = 0
    start_value = lst[ind]
    for index, value in enumerate(lst):
        if index == ind:
            continue
        if index < ind:
            if value < start_value:
                sum_left += value
        elif index > ind:
            if value < start_value:
                sum_right += value
    if sum_left >= sum_right:
        print(f"Left - {sum_left}")
    else:
        print(f"Right - {sum_right}")


def get_expensive(lst, ind):
    sum_left = 0
    sum_right = 0
    start_value = lst[ind]
    for index, value in enumerate(lst):
        if index == ind:
            continue
        if index < ind:
            if value >= start_value:
                sum_left += value
        elif index > ind:
            if value >= start_value:
                sum_right += value
    if sum_left >= sum_right:
        print(f"Left - {sum_left}")
    else:
        print(f"Right - {sum_right}")


price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
command = input()
if command == "cheap":
    get_cheap(price_ratings, entry_point)
elif command == "expensive":
    get_expensive(price_ratings, entry_point)
