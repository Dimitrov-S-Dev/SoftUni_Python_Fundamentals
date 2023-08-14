indexes = input().split()
text = list(input())
result = ''

for index in indexes:
    curr_index = 0
    for idx in index:
        curr_index += int(idx)

    char_index = curr_index % len(text)
    result += text[char_index]
    text.pop(char_index)

print(result)
