"""
Write a program that receives a number n on the first line.
On the following n lines, it receives different integer numbers.
If the program receives an odd number,
print "{num} is odd!" and end the program. Otherwise,
if all numbers given are even, print "All numbers are even.".
"""

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
