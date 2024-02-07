train_ticket = 150
items = input().split('|')
budget = float(input())
profit = 0
new_price = []
"""
clothes = 50.00
shoes = 35.00
accessories = 20.50
"""
condition = False
for item in items:
    info = item.split('->')
    item_type = info[0]
    price = float(info[1])
    condition = False
    if item_type == 'Clothes' and price <= 50:
        condition = True
    elif item_type == 'Shoes' and price <= 35:
        condition = True
    elif item_type == 'Accessories' and price <= 20.5:
        condition = True
    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.4
            rounded_price = round(price * 1.4, 2)
            new_price.append(rounded_price)

print(*new_price, sep=" ")
print(f"Profit: {profit:.2f}")
sum_of_all = sum(new_price)

if sum_of_all + budget > 150:
    print('Hello, France!')
else:
    print('Not enough money.')
