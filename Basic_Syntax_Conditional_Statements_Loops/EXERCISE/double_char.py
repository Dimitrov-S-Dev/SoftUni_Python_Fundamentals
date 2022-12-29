command = input()

while command != "End":
	result = ""
	for char in command:
		result += char * 2
	print(result)
	command = input()
