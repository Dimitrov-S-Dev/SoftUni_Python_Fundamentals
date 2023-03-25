def get_info(number):
    heroes_dict = {}
    for _ in range(number):
        hero_name, hp, mp = input().split()
        hp = int(hp)
        mp = int(mp)
        heroes_dict[hero_name] = {"HP":hp, "MP":mp}

    return heroes_dict


def get_while(heroes_dict):
    while True:
        command = input()
        if command == "End":
            break
        info = command.split(" - ")
        action = info[0]
        hero_name = info[1]

        if action == "CastSpell":
            mp_needed = int(info[2])
            spell_name = info[3]
            if heroes_dict[hero_name]["MP"] >= mp_needed:
                heroes_dict[hero_name]["MP"] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif action == "TakeDamage":
            damage = int(info[2])
            attacker = info[3]
            heroes_dict[hero_name]["HP"] -= damage
            if heroes_dict[hero_name]["HP"] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del heroes_dict[hero_name]

        elif action == "Recharge":
            amount = int(info[2])
            current_mp = heroes_dict[hero_name]["MP"]
            if heroes_dict[hero_name]["MP"] + amount > 200:
                heroes_dict[hero_name]["MP"] = 200
            else:
                heroes_dict[hero_name]["MP"] += amount
            diff = heroes_dict[hero_name]["MP"] - current_mp
            print(f"{hero_name} recharged for {diff} MP!")

        elif action == "Heal":
            amount = int(info[2])
            current_hp = heroes_dict[hero_name]["HP"]
            if heroes_dict[hero_name]["HP"] + amount > 100:
                heroes_dict[hero_name]["HP"] = 100
            else:
                heroes_dict[hero_name]["HP"] += amount
            diff = heroes_dict[hero_name]["HP"] - current_hp
            print(f"{hero_name} healed for {diff} HP!")

    return heroes_dict


def get_print(heroes_dict):
    for hero in heroes_dict.keys():
        print(hero)
        print(f"HP: {heroes_dict[hero]['HP']}")
        print(f"MP: {heroes_dict[hero]['MP']}")

def get_heroes(number):
    heroes_dict = get_info(number)
    heroes_dict = get_while(heroes_dict)
    get_print(heroes_dict)


n = int(input())
get_heroes(n)
