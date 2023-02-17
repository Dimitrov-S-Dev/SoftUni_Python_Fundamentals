def get_fire(warship, ind, dem):




def get_defend(pirate, ind):
    pass



def get_repair(pirate, ind, hlth):
    pass



def get_status(pirate):
    pass


def get_main(pirate, warship):
    while True:
        command = input()
        if command == "Retire":
            pass
        info = command.split()
        action = info[0]

        if action == "Fire":
            index = int(info[1])
            demage = int(info[2])
            if index in range(len(warship)):
                if warship[index] - demage <= 0:
                    print()
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