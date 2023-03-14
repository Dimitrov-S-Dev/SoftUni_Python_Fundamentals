number_of_students = int(input())
number_of_lectures = int(input())
bonus = int(input())

max_bonus = 0
attendances = 0

for attendance in range(1, number_of_students + 1):
    current_attendance = int(input())
    total_bonus = current_attendance / number_of_lectures * (5 + bonus)
    total_bonus = round(total_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendances = current_attendance

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {attendances} lectures.")
