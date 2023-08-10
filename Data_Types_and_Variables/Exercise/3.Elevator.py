persons = int(input())
number_of_people = int(input())
count = 0
if number_of_people != 0:
    for number in range(0, persons, number_of_people):
        count += 1

print(count)
