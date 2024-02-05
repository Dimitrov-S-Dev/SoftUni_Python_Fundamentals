budget = int(input())

condition = True
while True:
    command = input()
    if command == "End":
        break

    product_price = int(command)
    if product_price > budget:
        condition = False
        print("You went in overdraft!")
        break
    budget -= product_price

if condition:
    print("You bought everything needed.")
