animals = input().split(", ")[::-1]

for index, animal in enumerate(animals):
    if animal == "wolf":
        if index == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
