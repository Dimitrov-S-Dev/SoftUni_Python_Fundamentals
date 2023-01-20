# Task 1 Concat Names

first_name = input()
second_name = input()
delimiter = input()

print(f"{first_name}{delimiter}{second_name}")

# Task 2 Convert Meters to Kilometers

meters = int(input())
kilometers = meters / 1000

print(f"{kilometers:.2f}")

# Task 3 Pounds to Dollars

pounds = int(input())
dollars = pounds * 1.31

print(f"{dollars:.3f}")

# Task 4 Centuries to Minutes

centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

# Task 5 Special Numbers

count_iter = int(input())

for number in range(1, count_iter + 1):
    sum_of_digit = 0
    sum_of_digit += number % 10
    sum_of_digit += number // 10
    if sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 14:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")

# Task 6 Next Happy Year

year = int(input())

while True:
    year += 1
    year_to_str = str(year)
    set_year = set(year_to_str)
    if len(year_to_str) != len(set_year):
        continue
    else:
        print(year_to_str)
        break
