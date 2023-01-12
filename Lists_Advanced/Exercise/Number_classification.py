"""
Using a list comprehension, write a program that receives numbers,
separated by comma and space ", ",
and prints all the positive, negative, even,
and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
"""


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
