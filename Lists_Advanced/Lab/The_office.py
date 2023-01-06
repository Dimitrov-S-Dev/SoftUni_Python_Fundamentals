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

