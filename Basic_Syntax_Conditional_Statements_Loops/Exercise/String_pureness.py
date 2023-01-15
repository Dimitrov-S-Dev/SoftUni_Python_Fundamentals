"""
You will be given number n. After that, you'll receive different
strings n times. Your task is to check if the given strings are pure,
meaning that they do NOT consist any of the characters:
comma ",", period ".", or underscore "_":
· If a string is pure, print "{string} is pure."
· Otherwise, print "{string} is not pure!"
"""

count_iter = int(input())

for word in range(count_iter):
	current_word = input()
	if "," in current_word or "." in current_word or "_" in current_word:
		print(f"{current_word} is not pure!")
	else:
		print(f"{current_word} is pure.")
