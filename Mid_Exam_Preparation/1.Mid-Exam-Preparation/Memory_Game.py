def get_result(lst, indx1, indx2):
    if lst[indx1] == lst[indx2]:
        print(f"Congrats! You have found matching elements - {lst[indx1]}!")
        for index in range(len(lst) - 1, -1, -1):
            if index == indx2 or index == indx1:
                lst.pop(index)
    else:
        print("Try again!")
    return lst


def get_cheat(lst, move):
    middle = len(lst) // 2
    lst.insert(middle, f'-{move}a')
    lst.insert(middle, f'-{move}a')
    return lst


def get_main(lst):
    moves = 0
    while True:
        if len(lst) == 0:
            print(f"You have won in {moves} turns!")
            break
        moves += 1
        command = input()
        if command == "end":
            print("Sorry you lose :(")
            print(' '.join(lst))
            break
        info = command.split()
        index_one = int(info[0])
        index_two = int(info[1])
        if index_one not in range(len(lst)) or index_two not in range(len(lst)) or index_one == index_two:
            lst = get_cheat(lst, moves)
            print(f"Invalid input! Adding additional elements to the board")
        else:
            lst = get_result(lst, index_one, index_two)


elements = input().split()
get_main(elements)
