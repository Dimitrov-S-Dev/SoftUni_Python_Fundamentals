neighborhood = [int(x) for x in input().split("@")]
index = 0

command = input()

while command != "Love!":
    info = command.split()
    current_index = int(info[1])
    index += current_index
    if index >= len(neighborhood):
        index = 0
    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    result = [el for el in neighborhood if el != 0]
    print(f"Cupid has failed {len(result)} places.")
