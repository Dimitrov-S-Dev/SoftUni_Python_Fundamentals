def get_while(text):
    while True:
        command = input()
        if command == "Generate":
            break
        info = command.split(">>>")
        action = info[0]

        if action == "Contains":
            substring = info[1]
            if substring in text:
                print(f"{text} contains {substring}")
            else:
                print(f"Substring not found!")

        elif action == "Flip":
            upper_lower = info[1]
            start_index = int(info[2])
            end_index = int(info[3])
            if upper_lower == "Lower":
                text = text[0:start_index] + text[start_index:end_index].lower() + text[end_index:]
            elif upper_lower == "Upper":
                text = text[0:start_index] + text[start_index:end_index].upper() + text[end_index:]

            print(text)

        elif action == "Slice":
            start_index = int(info[1])
            end_index = int(info[2])
            text = text[0:start_index] + text[end_index:]

            print(text)

    return text


def get_print(activation_key):
    print(f"Your activation key is: {activation_key}")


def get_activation_keys(text):
    text = get_while(text)
    get_print(text)


data = input()
get_activation_keys(data)
