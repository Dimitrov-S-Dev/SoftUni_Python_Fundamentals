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
