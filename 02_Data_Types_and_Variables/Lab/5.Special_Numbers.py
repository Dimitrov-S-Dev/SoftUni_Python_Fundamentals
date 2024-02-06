for number in range(1, int(input()) + 1):
    sum_of_digit = 0
    digit = number
    while digit:
        last_num = digit % 10
        sum_of_digit += last_num
        digit = number // 10
    if sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
