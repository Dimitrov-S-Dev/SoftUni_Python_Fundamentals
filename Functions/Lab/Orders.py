def get_total(item, qty):
    if item == 'coffee':
        return qty * 1.5
    elif item == 'coke':
        return qty * 1.4
    elif item == 'water':
        return qty * 1.0
    elif item == 'snack':
        return qty * 2.0


product = input()
quantity = int(input())
print(get_total(product, quantity))
