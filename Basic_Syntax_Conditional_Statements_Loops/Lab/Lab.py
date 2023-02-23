# Task 1 Number Definer

number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number > 1_000_000:
        print("large positive")
    elif number < 1:
        print("small positive")
    else:
        print("positive")
else:
    if abs(number) > 1_000_000:
        print("large negative")
    elif abs(number) < 1:
        print("small negative")
    else:
        print("negative")

# Task 2 Largest of Three Numbers

first_num = int(input())
second_num = int(input())
third_num = int(input())
# if first_num > second_num and first_num > third_num:
# 	print(first_num)
# elif second_num > first_num and second_num > third_num:
# 	print(second_num)
# else:
# 	print(third_num)
print(max(first_num, second_num, third_num))

# Task 3 Word Reverse

word = input()
# reversed_word = ""
# for index in range(len(word) - 1, -1, -1):
# 	reversed_word += word[index]
# print(reversed_word)
reversed_word = word[::-1]
print(reversed_word)

# Task 4 Even Numbers

count_iter = int(input())
is_even = True

for _ in range(count_iter):
    number = int(input())
    if number % 2 != 0:
        is_even = False
        print(f"{number} is odd!")
        break

if is_even:
    print("All numbers are even.")

# Task 5.Mid-Exam-Preparation Number Between 1 and 100

while True:
    number = float(input())
    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break

# Task 6 Shopping

budget = int(input())
is_all_bought = True
command = input()

while command != "End":
    price = int(command)
    if budget >= price:
        budget -= price
    else:
        print("You went in overdraft!")
        is_all_bought = False
        break
    command = input()

if is_all_bought:
    print("You bought everything needed.")

# Task 7 Patterns

number = int(input())

for row1 in range(1, number + 1):
    print("*" * row1)

for row2 in range(number - 1, 0, - 1):
    print("*" * row2)
