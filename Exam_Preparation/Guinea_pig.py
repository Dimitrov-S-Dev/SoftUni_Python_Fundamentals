"""
On the first three lines, you will receive the quantity of food,
hay, and cover, which Merry buys for a month (30 days).
On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food.
Every second day Merry first feeds the pet,
then gives it a certain amount of hay equal to 5% of the rest of the food.
On every third day,
Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover,
will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!
· On the first line – quantity food in kilograms -
a floating-point number
· On the second line – quantity hay in kilograms -
a floating-point number
· On the third line – quantity cover in kilograms -
a floating-point number
· On the fourth line – guinea's weight in kilograms -
a floating-point number
"""


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

for day in range(1, 31):
    food_qty = get_food(food_qty)
    if day % 2 == 0:
        hay_qty = get_hay(hay_qty, food_qty)
    if day % 3 == 0:
        cover_qty = get_cover(cover_qty, pig_weight)

if food_qty > 0 and hay_qty > 0 and cover_qty > 0:
    food_qty /= 1000
    hay_qty /= 1000
    cover_qty /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_qty:.2f}, Hay: {hay_qty:.2f}, Cover: {cover_qty:.2f}.")
else:
    print(f"Merry must go to the pet store!")

