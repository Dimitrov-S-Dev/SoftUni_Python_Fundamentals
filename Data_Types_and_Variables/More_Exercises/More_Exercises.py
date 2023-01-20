# Task 1

first_num = int(input())
second_num = int(input())

print(f"Before:")
print(f"a = {first_num}")
print(f"b = {second_num}")
first_num, second_num = second_num, first_num
print(f"After:")
print(f"a = {first_num}")
print(f"b = {second_num}")

# Task 2

number = int(input())
is_prime = True

for num in range(2, number):
    if number % num == 0:
        print("False")
        is_prime = False
        break
if is_prime:
    print("True")

# Task 3

key = int(input())
count_iter = int(input())
message = ""

for _ in range(count_iter):
    current_letter = (input())
    ascid_num = ord(current_letter) + key
    message += chr(ascid_num)
print(message)

# Task 4

number_of_lines = int(input())
is_balanced = True
is_open = False

for _ in range(number_of_lines):
    char = input()
    if char == "(":
        if is_open:
            is_balanced = False
        else:
            is_open = True
    elif char == ")":
        if is_open:
            is_open = False
        else:
            is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
    