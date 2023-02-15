people = int(input())
lift_places = [int(x) for x in input().split()]
condition = False

for index, value in enumerate(lift_places):
    if value == 4:
        continue
    free = 4 - value
    if free < people:
        lift_places[index] += free
        people -= free
    else:
        lift_places[index] += people
        people -= free
        condition = True
        break

if condition:
    if sum(lift_places) < len(lift_places) * 4:
        print("The lift has empty spots!")
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(*lift_places, sep=" ")
