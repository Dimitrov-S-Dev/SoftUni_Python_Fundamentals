"""
You will be given a number.
Print the largest number that can be formed from
the digits of the given number.
"""

number = list(map(int, input()))
number.sort(reverse=True)
print(*number, sep="")
