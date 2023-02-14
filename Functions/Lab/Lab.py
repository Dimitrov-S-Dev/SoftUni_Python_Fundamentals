# Task 1 Absolute Values

# def abs_num(lst):
#     result = []
#     for num in lst:
#         result.append(abs(num))
#     return result
#
# numbers = list(map(float,input().split()))
# print(abs_num(numbers))

numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)

# Task 2 Grades


def get_grade(num):
    if 2 <= num <= 2.99:
        return 'Fail'
    elif num <= 3.49:
        return 'Poor'
    elif num <= 4.49:
        return 'Good'
    elif num <= 5.49:
        return 'Very Good'
    else:
        return 'Excellent'


grade = float(input())
print(get_grade(grade))

# Task 3 Calculations


def get_calculates(par,num1,num2):
    if par == 'multiply':
        return num1 * num2
    elif par == 'divide':
        return int(num1 / num2)
    elif par == 'add':
        return num1 + num2
    elif par == 'subtract':
        return num1 - num2


operator = input()
first_num = int(input())
second_num = int(input())
print(get_calculates(operator, first_num, second_num))

# Task 4 Repeat String

def get_repeat(text, num):
    return text * num


string = input()
number = int(input())
print(get_repeat(string, number))
# result = lambda string, num: string * num


#  Task 5.Mid-Exam-Preparation Orders

def get_total(item, qty):
    if item == 'coffee':
        return qty * 1.5
    elif item == 'coke':
        return qty * 1.4
    elif item == 'water':
        return qty * 1.0
    elif item == 'snack':
        return qty * 2.0


product = input()
quantity = int(input())
print(get_total(product, quantity))

# Task 6 Calculate Rectangle Area


def get_area(w, h):
    return w * h


width = int(input())
height = int(input())
print(get_area(width, height))

# Task 7 Rounding


def get_round(lst):
    rounds = []
    for num in lst:
        rounds.append(int(num))
    return rounds


numbers = list(map(float, input().split()))
print(get_round(numbers))
