employee_one_per_hour = int(input())
employee_two_per_hour = int(input())
employee_three_per_hour = int(input())
students_cunt = int(input())

total_employee_per_hour = employee_one_per_hour + employee_two_per_hour + employee_three_per_hour
hours = 0

while students_cunt > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    if students_cunt > total_employee_per_hour:
        students_cunt -= total_employee_per_hour
    else:
        students_cunt -= students_cunt
    if students_cunt == 0:
        break

print(f"Time needed: {hours}h.")
