"""
On the first line, you will be given how many rows there are in the maze.
On the following n lines, you will be given the maze itself.
Here is a legend for the maze:
· "#" - means a wall; Kate cannot go through there
· " " - means empty space; Kate can go through there
· "k" - the initial position of Kate; start looking for a way out from there.
There are two options: Kate either gets out or not:
· If Kate can get out, print the following: "Kate got out in {number_of_moves} moves".
Note: If there are two or more ways out, she always chooses the longest one.
· Otherwise, print: "Kate cannot get out".
"""


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
