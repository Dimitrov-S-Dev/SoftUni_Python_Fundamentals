def sum_numbers(a, b):
    return a + b


def subtract(d, c):
    return d - c


def add_and_subtract(a, b, c):
    sum_first_second = sum_numbers(a, b)
    result = subtract(sum_first_second, c)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
