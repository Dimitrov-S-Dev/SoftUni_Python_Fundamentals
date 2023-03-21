def get_while(message):
    while True:
        command = input()
        if command == "Reveal":
            break
        info = command.split(":|:")
        action = info[0]

        if action == "InsertSpace":
            index = int(info[1])
            message = message[0:index] + " " + message[index:]
            print(message)

        elif action == "Reverse":
            substring = info[1]
            if substring in message:
                message = message.strip(substring)
                message += substring[::-1]
                print(message)
            else:
                print(f"error")

        elif action == "ChangeAll":
            substring = info[1]
            replacement = info[2]
            message = message.replace(substring, replacement)
            print(message)

    return message


def get_print(message):
    print(f"You have a new text message: {message}")

def get_secret_chat(message):
    message = get_while(message)
    get_print(message)


data = input()
get_secret_chat(data)

