# Task 1

number = list(map(int, input()))
number.sort(reverse=True)
print(*number, sep="")

# Task 2

text = input()
result = []

for index, value in enumerate(text):
    if value.isupper():
        result.append(index)

print(result)

# Task 3

animals = input().split(", ")

for index, value in enumerate(reversed(animals)):
    if value == "wolf" and index == 0:
        print("Pls go away and stop eating my sheep.")
    elif value == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

# Task 4

text = input().lower()
searched_words = ["sand", "water", "fish", "sun"]
counts = 0

for word in searched_words:
    if word in text:
        count = text.count(word)
        counts += count

print(counts)
