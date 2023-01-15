"""
You will be given strings until you receive the command "End".
For each string given, you should print a string in which
each character (case-sensitive) is repeated twice.
Note that if you receive the string "SoftUni",
you should NOT print it!
"""

while True:
	command = input()
	if command == "End":
		break
	if command == "SoftUni":
		continue
	result = ""
	for char in command:
		result += char * 2
	print(result)
