def get_negative_positive(lst):
    for digit in lst:
        if digit < 0:
            return True
    return False


first_num = int(input())
second_num = int(input())
third_num = int(input())
number_lst = [first_num, second_num, third_num]

if get_negative_positive(number_lst):
    print("negative")
else:
    print("positive")
