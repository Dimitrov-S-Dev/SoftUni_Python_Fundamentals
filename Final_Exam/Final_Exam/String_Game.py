def get_string_game(text):
    while True:
        command = input()
        if command == "Done":
            break
        info = command.split()
        action = info[0]

        if action == "Change":
            char = info[1]
            replacement = info[2]
            text = text.replace(char, replacement)
            print(text)

        elif action == "Includes":
            substring = info[1]
            if substring in text:
                print("True")
            else:
                print("False")

        elif action == "End":
            substring = info[1]
            if text.endswith(substring):
                print("True")
            else:
                print("False")

        elif action == "Uppercase":
            text = text.upper()
            print(text)

        elif action == "FindIndex":
            char = info[1]
            index = text.index(char)
            print(index)

        elif action == "Cut":
            start_index = int(info[1])
            count = int(info[2])
            end_index = start_index + count
            text = text[start_index:end_index]
            print(text)


data = input()
get_string_game(data)
