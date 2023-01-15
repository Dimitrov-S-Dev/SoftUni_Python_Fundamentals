"""
Beaches are filled with sand, water, fish, and sun.
Given a string, calculate how many times the words
"Sand", "Water", "Fish", and "Sun" appear (case insensitive)
"""

text = input().lower()
searched_words = ["sand", "water", "fish", "sun"]
counts = 0

for word in searched_words:
	if word in text:
		count = text.count(word)
		counts += count
print(counts)
