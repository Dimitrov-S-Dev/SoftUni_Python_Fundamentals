# Task 1 Reverse String

def get_main(lst):
    for word in lst:
        print(f"{word} = {word[::-1]}")


words = []

while True:
    command = input()
    if command == "end":
        break
    words.append(command)

get_main(words)

# Task 2 Repeat String

string = input().split()

result = [el * len(el) for el in string]
print("".join(result))

# Task 3 Substring

first = input()
second = input()

while first in second:
    second = second.replace(first, "")

print(second)

# Task 4 Text Filer

banned_words = input().split(", ")
text = input("""""")

for word in banned_words:
    text = text.replace(word, "*" * len(word))

print(text)

# Task 5 Digits, Letters and Others

string = input()
digit = ""
letter = ""
other = ""
for char in string:
    if char.isdigit():
        digit += char
    elif char.isalpha():
        letter += char
    else:
        other += char

print(digit)
print(letter)
print(other)
