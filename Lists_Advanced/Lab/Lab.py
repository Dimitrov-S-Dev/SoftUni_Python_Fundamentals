# Task 1 No vowels

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [x for x in text if x.lower() not in vowels]
print(''.join(result))

# Task 2 Trains

def get_inset(lst, i, num):
    lst[i] += num
    return lst


def get_leave(lst, i, num):
    lst[i] -= num
    return lst


wagons_count = int(input())
train = [0] * wagons_count

command = input()

while command != 'End':
    info = command.split()
    action = info[0]
    if action == 'add':
        train[-1] += int(info[1])

    elif action == 'insert':
        index = int(info[1])
        people = int(info[2])
        get_inset(train, index, people)

    elif action == 'leave':
        index = int(info[1])
        people = int(info[2])
        get_leave(train, index, people)
    command = input()

print(train)

# Task 3 To-do List

# command = input()
# importance_lst = [0] * 10
#
# while command != 'End':
#     ind, note = command.split('-')
#     index = int(ind) - 1
#     importance_lst[index] = note
#     command = input()
#
# print([x for x in importance_lst if x != 0])
command = input()
tasks_lst = []

while command != 'End':
    priority, note = command.split('-')
    priority = int(priority)
    tasks_lst.append((priority, note))
    command = input()

result = [x[1] for x in sorted(tasks_lst)]
print(result)

# Task 4 Palindrome strings

words = input().split()
searched_word = input()

palindromes = [x for x in words if x == x[:: -1]]
count = palindromes.count(searched_word)

print(palindromes)
print(f"Found palindrome {count} times")

# Task 5 Sorting names

names = input().split(', ')
result = sorted(names, key=lambda item: (-len(item), item))
print(result)


# Task 6 Even numbers

numbers = list(map(int, input().split(', ')))
result = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(result)

#  Task 7 The office

nums = [int(el) for el in input().split()]
factor = int(input())
happiness = [el * factor for el in nums]
avg = sum(happiness) / len(happiness)

happy_employee = [el for el in happiness if el >= avg]
sad_employee = [el for el in happiness if el < avg]

happy_message = "Employees are happy!"
not_happy_message = "Employees are not happy!"

if len(sad_employee) > len(happiness) / 2:
    print(f"Score: {len(happy_employee)}/{len(happiness)}. {not_happy_message}")
else:
    print(f"Score: {len(happy_employee)}/{len(happiness)}. {happy_message}")
