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
print(get_calculates(operator,first_num,second_num))




