def get_factorial(num):
    for current_number in range(1, num):
        num *= current_number
    return num


first_num = int(input())
second_num = int(input())
result = get_factorial(first_num) / get_factorial(second_num)
print(f"{result:.2f}")

