budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
bread_price = flour_price + eggs_price + milk_price
number_of_loaves = 0
colored_eggs = 0

while True:
    if budget < bread_price:
        break
    budget -= bread_price
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        if colored_eggs < number_of_loaves - 2:
            break
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
