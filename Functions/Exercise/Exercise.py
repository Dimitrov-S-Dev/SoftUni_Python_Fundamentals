# Task 1 Smallest of Three Numbers

def get_smallest(lst):
    return min(lst)


num1 = int(input())
num2 = int(input())
num3 = int(input())

all_numbers = [num1, num2, num3]
print(get_smallest(all_numbers))

# Task 2 Add and Subtract

def sum_numbers(a, b):
    return a + b


def subtract(d, c):
    return d - c


def add_and_subtract(a, b, c):
    sum_first_and_second = sum_numbers(a, b)
    result = subtract(sum_first_and_second, c)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))

# Task 3 Characters in range


def get_character(a, b):
    characters = []
    for current_char in range(ord(a) + 1, ord(b)):
        characters.append(chr(current_char))
    return characters


first_char = input()
second_char = input()
result = get_character(first_char, second_char)
print(' '.join(result))
# print(*result)

# Task 4 Odd and even sum

def get_sum_numbers(number):
    evens = 0
    odds = 0
    for elem in number:
        num = int(elem)
        if num % 2 == 0:
            evens += num
        else:
            odds += num
    return evens, odds


number_as_str = input()
sum_even, sum_odd = get_sum_numbers(number_as_str)
print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

# Task 5 Even Numbers

def get_evens(lst):
    evens = []
    for number in lst:
        if number % 2 == 0:
            evens.append(number)
    return evens


numbers = list(map(int, input().split()))
print(get_evens(numbers))


# Task 6 Sort

numbers = list(map(int, input().split()))
result = sorted(numbers)
print(result)


# Task 7 Min max and sum

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

# Task 8 Palindrome integers

def get_palindrome(num):
    return num == num[:: -1]


numbers_as_str = input().split(', ')
for number in numbers_as_str:
    print(get_palindrome(number))


# Task 9 Password validator

def get_password_valid(word):
    is_valid = []
    if len(word) < 6 or len(word) > 10:
        is_valid.append('Password must be between 6 and 10 characters')
    if not word.isalnum():
        is_valid.append('Password should have only letters and digits')
    count = 0
    for elem in word:
        if elem.isdigit():
            count += 1
    if count < 2:
        is_valid.append('Password must have at least 2 digits')
    return is_valid


password = input()
password_validation = get_password_valid(password)
if len(password_validation) > 0:
    print('\n'.join(password_validation))
else:
    print('Password is valid')

# Task 10 Perfect number

def get_perfect_number(num):
    sum_digit = 0
    for digit in range(1, num):
        if num % digit == 0:
            sum_digit += digit
    if sum_digit == num:
        return f'We have a perfect number!'
    return f"It's not so perfect."


number = int(input())
print(get_perfect_number(number))


# Task 11 Loading bar

def get_loading_bar(num):
    if num == 100:
        return f"100% Complete!\n [%%%%%%%%%%]"
    return f"{num}% [{'%' * (num//10)}{'.' * (10 - num// 10)}]\n Still loading..."


number = int(input())
print(get_loading_bar(number))


# Task 12 Factorial division

def get_factorial(num):
    for current_number in range(1, num):
        num *= current_number
    return num


first_num = int(input())
second_num = int(input())
result = get_factorial(first_num) / get_factorial(second_num)
print(f"{result:.2f}")
