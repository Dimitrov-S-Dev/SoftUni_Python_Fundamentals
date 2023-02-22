# Task 1 Bakery

items = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value

print(bakery)


# Task 2 Stock

items = input().split()
search_products = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value

for product in search_products:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# Task 3 Statistics



