def get_evens(lst):
    evens = []
    for number in lst:
        if number % 2 == 0:
            evens.append(number)
    return evens


numbers = list(map(int, input().split()))
print(get_evens(numbers))
