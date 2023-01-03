count_iter = int(input())

for number in range(1, count_iter + 1):
    sum_of_digit = 0
    sum_of_digit += number % 10
    sum_of_digit += number // 10
    if sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 14:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
