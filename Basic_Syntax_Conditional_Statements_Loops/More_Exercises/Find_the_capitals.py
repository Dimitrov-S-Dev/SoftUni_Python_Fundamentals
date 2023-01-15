"""
Write a program that takes a single string
and prints a list of all the capital letters indices.
"""

text = input()
result = []

for index, value in enumerate(text):
	if value.isupper():
		result.append(index)
print(result)
