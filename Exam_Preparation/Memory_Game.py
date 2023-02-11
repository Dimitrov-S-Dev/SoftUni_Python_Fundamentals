def get_equal(lst, indx1, indx2):
    if lst[indx1] == lst[indx2]:
        print(f"Congrats! You have matching elements -{lst[indx1]}! ")
        for index in range(len(lst) - 1, -1, -1):
            if index == indx1 or index == indx2:
                lst.pop(index)
    else:
        print("Try again!")
    return lst


def get_cheat(lst, number):
    middle = len(lst) // 2
    lst.insert(middle, f"{number}a")
    lst.insert(middle, f"{number}a")
    print("Invalid input! Adding additional elements to the board")
    return lst


def get_main(lst):
    turns = 0
    condition = False
    while True:
        command = input()
        if command == "end":
            break
        if not lst:
            condition = True
            break
        turns += 1
        info = command.split()
        index_1 = int(info[0])
        index_2 = int(info[1])
        if index_2 == index_1 or index_1 not in range(len(lst)) or index_2 not in range(len(lst)):
            lst = get_cheat(lst, turns)
        else:
            lst = get_equal(lst, index_1, index_2)
    if condition:
        return f"You have won it {turns} turns!"
    else:
        return f"Sorry you lose :( \n {' '.join(lst)}"


numbers = input().split()
print(get_main(numbers))
