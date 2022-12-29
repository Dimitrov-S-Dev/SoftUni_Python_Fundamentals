count_iter = int(input())
is_even = True
for _ in range(count_iter):
	number = int(input())
	if number % 2 != 0:
		is_even = False
		print(f"{number} is odd!")
		break
if is_even:
	print("All numbers are even")
