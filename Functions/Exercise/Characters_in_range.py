def get_character(a, b):
    characters = []
    for current_char in range(ord(a) + 1, ord(b)):
        characters.append(chr(current_char))
    return characters


first_char = input()
second_char = input()
result = get_character(first_char, second_char)
print(' '.join(result))
# print(*result)
