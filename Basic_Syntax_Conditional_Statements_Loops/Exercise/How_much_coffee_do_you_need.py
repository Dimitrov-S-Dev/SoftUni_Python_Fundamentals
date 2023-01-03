command = input()
coffee_count = 0

while command.lower() != "end":
	if "coding" in command.lower() or "dog" in command.lower() or "cat" in command.lower() \
		or "movie" in command.lower():
		if command.isupper():
			coffee_count += 2
		else:
			coffee_count += 1
	if coffee_count > 5:
		print("You need extra sleep")
	command = input()
print(coffee_count)
