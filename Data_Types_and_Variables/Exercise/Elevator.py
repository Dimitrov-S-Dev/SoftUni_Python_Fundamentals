from math import ceil

persons = int(input())
capacity = int(input())
courses = 0
if courses != 0:
    courses = ceil(persons / capacity)

print(courses)
