health = 100
bitcoins = 0
rooms = input().split("|")
best_room = 0
condition = False

for room in rooms:
    best_room += 1
    info = room.split()
    command = info[0]
    number = int(info[1])

    if command == "potion":
        current_health = health
        if current_health + number > 100:
            heal_up = 100 - current_health
            health = 100
        else:
            heal_up = number
            health += heal_up
        print(f"You healed for {heal_up} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        if health - number <= 0:
            print(f"You died! Killed by {command}.")
            condition = True
            break
        else:
            health -= number
            print(f"You slayed {command}.")

if condition:
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
