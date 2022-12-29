first_word = input()
second_word = input()
final_word = first_word

for index in range(len(first_word)):
	left_part = second_word[: index + 1]
	right_part = first_word[index + 1:]
	current_word = left_part + right_part
	if current_word == final_word:
		continue
	print(current_word)
	final_word = current_word

