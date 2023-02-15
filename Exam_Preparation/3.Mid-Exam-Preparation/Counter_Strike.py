energy = int(input())
battles_won = 0
command = input()
condition = True

while command != "End of battle":
    distance = int(command)
    if distance > energy:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        condition = False
        break
    else:
        energy -= distance
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won
    command = input()

if condition:
    print(f"Won battles: {battles_won}. Energy left: {energy}" )
