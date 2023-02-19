from math import ceil
budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
free_pack = 0
if students > 4:
    free_pack = students // 5


result = apron_price * ceil(students * 1.2)
result += (egg_price * 10 * students)
result += flour_price * (students - free_pack)

if result <= budget:
    print(f"Items purchased for {result:.2f}$.")
else:
    diff = result - budget
    print(f"{diff:.2f}$ more needed.")
