n = int(input())
search_word = input()
result = []
word_in_result = []

for _ in range(n):
    current_word = input()
    if search_word in current_word:
        word_in_result.append(current_word)
    result.append(current_word)

print(result)
print(word_in_result)
