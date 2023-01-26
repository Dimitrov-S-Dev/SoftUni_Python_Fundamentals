# Task 1 Which Are In?

first = input().split(", ")
second = input().split(", ")
result = []

for w1 in first:
    for w2 in second:
        if w1 in w2 and w1 not in result:
            result.append(w1)

print(result)

# Task 2 Next Version


def get_version(lst):
    version_int = int("".join(lst)) + 1
    version_lst = [num for num in str(version_int)]
    print(".".join(version_lst))


version_str = input().split(".")
get_version(version_str)

# Task 3 Word Filter

text = input().split()
result = [el for el in text if len(el) % 2 == 0]

for word in result:
    print(word)

# Task 4 Number Classification


def get_positive(lst):
    result = [str(el) for el in lst if el >= 0]
    return ", ".join(result)


def get_negative(lst):
    result = [str(el) for el in lst if el < 0]
    return ", ".join(result)


def get_even(lst):
    result = [str(el) for el in lst if el % 2 == 0]
    return ", ".join(result)


def get_odd(lst):
    result = [str(el) for el in lst if el % 2 != 0]
    return ", ".join(result)


numbers = list(map(int, input().split(", ")))

print(f"Positive: {get_positive(numbers)}")
print(f"Negative: {get_negative(numbers)}")
print(f"Even: {get_even(numbers)}")
print(f"Odd: {get_odd(numbers)}")

# Task 5 Office Chairs

count_iter = int(input())
free_chairs = 0
condition = True

for room in range(1, count_iter + 1):
    current_room = input().split()
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    if chairs < visitors:
        diff = visitors - chairs
        print(f"{diff} more chairs needed in room {room}")
        condition = False
    else:
        free_chairs += chairs - visitors

if condition:
    print(f"Game On, {free_chairs} free chairs left")

# Task 6 Electron Distribution


def get_electron(num):
    result = []
    count = 0
    while num:
        count += 1
        position = 2 * count ** 2
        if num > position:
            result.append(position)
            num -= position
        else:
            result.append(num)
            num = 0
    return result


electron = int(input())
print(get_electron(electron))


