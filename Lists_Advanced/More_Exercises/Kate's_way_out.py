def get_start(lst):
    for index, value in enumerate(lst, 1):
        if value == "k":
            return len(lst) - index


def get_end(lst):
    for index, value in enumerate(lst):
        if value == " ":
            return index


number = int(input())
is_looking_way_out = False
cannot_go_out = False
moves = 0

for _ in range(number):
    current_move = list(input())

    if "k" in current_move:
        is_looking_way_out = True
        moves += get_start(current_move)
        continue
    if " " in current_move and is_looking_way_out:
        moves += get_end(current_move)

    if is_looking_way_out and " " not in current_move:
        print("Kate cannot get out")
        cannot_go_out = True
        break

if not cannot_go_out:
    print(f"Kate got out in {moves} moves")
