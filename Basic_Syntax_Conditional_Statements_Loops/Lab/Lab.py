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
