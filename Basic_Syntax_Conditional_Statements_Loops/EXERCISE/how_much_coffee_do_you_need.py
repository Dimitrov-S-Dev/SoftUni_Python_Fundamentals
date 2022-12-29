command = input()
coffee_count = 0
while command.lower() != "end":
	if "coding" in command or "dog" in command or "cat" in command \
		or "movie" in command:
		for char in command:
			if char.isupper():
				coffee_count += 2
			else:
				coffee_count += 1
	if coffee_count > 5:
		print("You need extra sleep")
	command = input()
print(coffee_count)
