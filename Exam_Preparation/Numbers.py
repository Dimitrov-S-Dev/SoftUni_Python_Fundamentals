"""
Write a program to read a sequence of integers and find and print
the top 5 numbers greater than the average value in the sequence,
sorted in descending order.
"""


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
new_lst = [el for el in sorted(numbers, reverse=True) if el > average]
if average == 1:
    print("No")
else:
    print(get_result(new_lst))
