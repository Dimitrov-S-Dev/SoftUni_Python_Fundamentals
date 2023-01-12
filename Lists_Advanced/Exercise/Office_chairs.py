count_iter = int(input())
free_chairs = 0
condition = True

for room in range(1, count_iter + 1):
    current_room = input().split()
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    if chairs < visitors:
        diff = visitors - chairs
        print(f"{diff} more chairs needed in room {room}")
        condition = False
    else:
        free_chairs += chairs - visitors

if condition:
    print(f"Game On, {free_chairs} free chairs left")
