def get_result(lst):
    result = []
    if len(lst) > 5:
        count = 5
    else:
        count = len(lst)
    for index in range(count):
        result.append(str(lst[index]))

    return f"{' '.join(result)}"


numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
greater_then_average = [el for el in sorted(numbers, reverse=True) if el > average]
if len(greater_then_average) == 0:
    print("No")
else:
    print(get_result(greater_then_average))
