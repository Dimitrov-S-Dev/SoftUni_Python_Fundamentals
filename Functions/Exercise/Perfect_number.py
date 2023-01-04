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
