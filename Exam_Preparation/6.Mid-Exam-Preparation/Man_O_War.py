def get_fire(warship, ind, dem):
    warship[ind] -= dem
    return warship


def get_defend(pirate, ind1, ind2, dem):
    for index in range(ind1, ind2 + 1):
        pirate[index] -= dem

    return pirate


def get_repair(pirate, ind, hlth):
    if ind in range(len(pirate)):
        if pirate[ind] + hlth > max_health:
            pirate[ind] = max_health
        else:
            pirate[ind] += hlth
    return pirate


def get_status(pirate):
    stat = max_health * 0.2
    count = 0
    for num in pirate:
        if num < stat:
            count += 1
    print(f"{count} sections need repair.")


def get_main(pirate, warship):
    while True:
        command = input()
        if command == "Retire":
            if sum(pirate) != sum(warship):
                pirate_info = f"Pirate ship status: {sum(pirate)}"
                warship_info = f"Warship status: {sum(warship)}"
                return f"{pirate_info}\n {warship_info}"
        info = command.split()
        action = info[0]

        if action == "Fire":
            index = int(info[1])
            damage = int(info[2])
            if index in range(len(warship)):
                if warship[index] - damage <= 0:
                    return f"You won! The enemy ship has sunken."
                else:
                    warship = get_fire(warship, index, damage)

        elif action == "Defend":
            start_index = int(info[1])
            end_index = int(info[2])
            damage = int(info[3])
            if start_index in range(len(pirate)) and end_index in range(len(pirate)):
                for idx in range(start_index, end_index + 1):
                    if pirate[idx] - damage <= 0:
                        return f"You lost! The pirate ship has sunken."
                pirate = get_defend(pirate, start_index, end_index, damage)

        elif action == "Repair":
            index = int(info[1])
            health = int(info[2])
            pirate = get_repair(pirate, index, health)
        elif action == "Status":
            get_status(pirate)


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health = int(input())
print(get_main(pirate_ship, war_ship))
