first_num = int(input())
second_num = int(input())

print(f"Before:")
print(f"a = {first_num}")
print(f"b = {second_num}")
first_num, second_num = second_num, first_num
print(f"After:")
print(f"a = {first_num}")
print(f"b = {second_num}")
