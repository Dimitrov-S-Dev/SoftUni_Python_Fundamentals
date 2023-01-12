house_number = list(map(int, input().split("@")))
index = 0

while True:
    command = input()
    if command == "Love!":
        break
    info = command.split()
    jump = int(info[1])
    current_index = index + jump

    if current_index >= len(house_number):
        current_index = 0
    if house_number[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        house_number[current_index] -= 2
        if house_number[current_index] == 0:
            print(f"Place {current_index} has a Valentine's day")

    index = current_index

print(f"Cupid's last position was {index}")

mission = [el for el in house_number if el != 0]
if len(mission) > 0:
    print(f"Cupid has failed {len(mission)} places.")
else:
    print(f"Mission was successful.")
