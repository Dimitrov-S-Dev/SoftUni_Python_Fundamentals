def get_food(food):
    food -= 300
    return food


def get_hay(hay, food):
    hay -= food * 0.05
    return hay


def get_cover(cover, weight):
    cover -= weight / 3
    return cover


food_qty = float(input()) * 1000
hay_qty = float(input()) * 1000
cover_qty = float(input()) * 1000
pig_weight = float(input()) * 1000

flag = False

for day in range(1, 31):
    food_qty = get_food(food_qty)
    if day % 2 == 0:
        hay_qty = get_hay(hay_qty, food_qty)
    if day % 3 == 0:
        cover_qty = get_cover(cover_qty, pig_weight)
    if food_qty <= 0 or hay_qty <= 0 or cover_qty <= 0:
        flag = True
        break
if flag:
    print(f"Merry must go to the pet store!")
else:
    food_qty /= 1000
    hay_qty /= 1000
    cover_qty /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_qty:.2f}, Hay: {hay_qty:.2f}, Cover: {cover_qty:.2f}.")
