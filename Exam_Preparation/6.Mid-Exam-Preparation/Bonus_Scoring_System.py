number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0

for student in range(number_of_students):
    total_bonus = 0
    current_attendance = int(input())
    total_bonus += round((current_attendance) / (number_of_lectures) * (5 + additional_bonus))
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = current_attendance

print(f"Max Bonus:{max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")
