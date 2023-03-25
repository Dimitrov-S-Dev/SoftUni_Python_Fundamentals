def get_while(text):
    while True:
        command = input()
        if command == "Done":
            break
        info = command.split()
        action = info[0]

        if action == "TakeOdd":
            new_text = ""
            for index in range(len(text)):
                if index % 2 != 0:
                    new_text += text[index]
            text = new_text
            print(text)

        elif action == "Cut":
            index = int(info[1])
            length = int(info[2])
            end = index + length
            text = text[:index] + text[end:]
            print(text)

        elif action == "Substitute":
            substring = info[1]
            substitute = info[2]
            if substring in text:
                text = text.replace(substring, substitute)
                print(text)
            else:
                print(f"Nothing to replace!")

    return text


def get_print(password):
    print(f"Your password is: {password}")

def get_password_reset(text):
    text = get_while(text)
    get_print(text)



data = input()
get_password_reset(data)
