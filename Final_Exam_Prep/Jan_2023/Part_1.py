# Task 1 The Limitation Game

def get_while(message):
    while True:
        command = input()
        if command == "Decode":
            break
        info = command.split("|")
        action = info[0]

        if action == "Move":
            num_letters = int(info[1])
            message = message[num_letters:] + message[0:num_letters]

        elif action == "Insert":
            index = int(info[1])
            value = info[2]
            message = message[0:index] + value + message[index:]

        elif action == "ChangeAll":
            substring = info[1]
            replacement = info[2]
            message = message.replace(substring, replacement)

    return message


def get_print(message):
    print(f"The decrypted message is: {message}")


def get_limitation(message):
    message = get_while(message)
    get_print(message)



data = input()
get_limitation(data)
