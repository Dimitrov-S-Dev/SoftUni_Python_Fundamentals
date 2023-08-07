while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue

    word = ""
    for char in command:
        word += char * 2
    print(word)
