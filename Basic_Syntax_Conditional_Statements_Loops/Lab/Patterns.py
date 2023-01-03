number = int(input())

for row1 in range(1, number + 1):
	print("*" * row1)

for row2 in range(number - 1, 0, - 1):
	print("*" * row2)
