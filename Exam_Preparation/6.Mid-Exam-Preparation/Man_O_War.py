











def get_main(p_lst, w_lst):
    while True:
        command = input()
        if command == "Retire":
            pass
        info = command.split()
        action = info[0]

        if action == "Fire":
            pass
        elif action == "Defend":
            pass
        elif action == "Repair":
            pass
        elif action == "Status":
            pass





pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())
get_main(pirate_ship)