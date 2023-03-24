def get_while(text):
    while True:
        command = input()
        if command == "Travel":
            break
        info = command.split(":")
        action = info[0]

        if action == "Add Stop":
            index = int(info[1])
            string = info[2]
            if index in range(len(text)):
                text = text[0:index] + string + text[index:]
            print(text)

        elif action == "Remove Stop":
            start_index = int(info[1])
            end_index = int(info[2])
            if start_index in range(len(text)) and end_index in range(len(text)):
                text = text[0:start_index] + text[end_index + 1:]
            print(text)

        elif action == "Switch":
            old_str = info[1]
            new_str = info[2]
            if old_str in text:
                text = text.replace(old_str, new_str)
            print(text)

    return text


def get_print(string):
    print(f"Ready for world tour! Planned stops: {string}")


def get_world_tour(text):
    text = get_while(text)
    get_print(text)


data = input()
get_world_tour(data)
