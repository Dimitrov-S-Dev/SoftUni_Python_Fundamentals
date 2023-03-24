def get_info(number):
    plant_d = {}
    for _ in range(number):
        plant, rarity = input().split("<->")
        rarity = int(rarity)

        if plant not in plant_d.keys():
            plant_d[plant] = {"rarity": 0, "rating": []}
        plant_d[plant]["rarity"] += rarity

    return plant_d


def get_while(plant_dict):
    while True:
        command = input()
        if command == "Exhibition":
            break
        info = command.split(": ")
        action = info[0]

        if action == "Rate":
            plant, rating = info[1].split(" - ")
            rating = int(rating)
            if plant in plant_dict.keys():
                plant_dict[plant]["rating"].append(rating)
            else:
                print(f"error")

        elif action == "Update":
            plant, rarity = info[1].split(" - ")
            rarity = int(rarity)
            if plant in plant_dict.keys():
                plant_dict[plant]["rarity"] = rarity
            else:
                print(f"error")

        elif action == "Reset":
            plant = info[1]
            if plant in plant_dict.keys():
                plant_dict[plant]["rating"] = []
            else:
                print(f"error")

    return plant_dict


def get_print(dict):
    print("Plants for the exhibition:")
    for plants in dict.keys():
        if len(dict[plants]["rating"]) > 0 and sum(dict[plants]["rating"]) > 0:
            avg = sum(dict[plants]["rating"]) / len(dict[plants]["rating"])
        else:
            avg = 0
        print(f"- {plants}; Rarity: {dict[plants]['rarity']}; Rating: {avg:.2f}")


def get_plant(number):
    plant_dict = get_info(number)
    plant_dict = get_while(plant_dict)
    get_print(plant_dict)


n = int(input())
get_plant(n)
