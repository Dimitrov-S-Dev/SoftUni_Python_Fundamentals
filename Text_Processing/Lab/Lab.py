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