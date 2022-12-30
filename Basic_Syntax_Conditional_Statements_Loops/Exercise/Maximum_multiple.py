divisor = int(input())
boundary = int(input())

for num in range(boundary, divisor, -1):
	if num % divisor == 0:
		print(num)
		break

# result = (boundary // divisor) * divisor
