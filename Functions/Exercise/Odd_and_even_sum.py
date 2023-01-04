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
