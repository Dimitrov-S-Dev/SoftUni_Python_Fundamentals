text = input().lower()
searched_words = ["sand", "water", "fish", "sun"]
counts = 0
for word in searched_words:
	if word in text:
		count = text.count(word)
		counts += count
print(counts)
