"""
You will receive two lines of input:
•a list of employees' happiness as a string of numbers
separated by a single space
•a happiness improvement factor (single number).
Your task is to find out if the employees are
generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•If half or more of the employees have happiness
greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
"""

nums = [int(el) for el in input().split()]
factor = int(input())
happiness = [el * factor for el in nums]
avg = sum(happiness) / len(happiness)

happy_employee = [el for el in happiness if el >= avg]
sad_employee = [el for el in happiness if el < avg]

happy_message = "Employees are happy!"
not_happy_message = "Employees are not happy!"

if len(sad_employee) > len(happiness) / 2:
    print(f"Score: {len(happy_employee)}/{len(happiness)}.{not_happy_message}")
else:
    print(f"Score: {len(happy_employee)}/{len(happiness)}.{happy_message}")
