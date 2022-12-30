animals = input().split(", ")

for index, value in enumerate(reversed(animals)):
	if value == "wolf" and index == 0:
		print("Please go away and stop eating my sheep.")
	elif value == "wolf":
		print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
