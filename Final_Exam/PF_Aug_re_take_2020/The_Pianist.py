def get_info(number):
    pianist_dict = {}
    for _ in range(number):
        piece, composer, key = input().split("|")
        pianist_dict[piece] = {"composer":composer, "key": key}

    return pianist_dict


def get_while(pianist_dict):
    while True:
        command = input()
        if command == "Stop":
            break
        info = command.split("|")
        action = info[0]
        piece = info[1]

        if action == "Add":
            composer = info[2]
            key = info[3]
            if piece in pianist_dict.keys():
                print(f"{piece} is already in the collection!")
            else:
                pianist_dict[piece] = {"composer": composer, "key": key}
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif action == "Remove":
            if piece in pianist_dict.keys():
                del pianist_dict[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")


        elif action == "ChangeKey":
            new_key = info[2]
            if piece in pianist_dict.keys():
                pianist_dict[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

    return pianist_dict


def get_print(pianist_dict):
    for piece in pianist_dict.keys():
        print(f"{piece} -> Composer: {pianist_dict[piece]['composer']}, Key: {pianist_dict[piece]['key']}")


def get_pianist(number):
    pianist_dict = get_info(number)
    pianist_dict = get_while(pianist_dict)
    get_print(pianist_dict)


n = int(input())
get_pianist(n)
