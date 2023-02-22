# # Task 1 Bakery
#
# items = input().split()
# bakery = {}
#
# for index in range(0, len(items), 2):
#     key = items[index]
#     value = int(items[index + 1])
#     bakery[key] = value
#
# print(bakery)
#
#
# # Task 2 Stock
#
# items = input().split()
# search_products = input().split()
# bakery = {}
#
# for index in range(0, len(items), 2):
#     key = items[index]
#     value = int(items[index + 1])
#     bakery[key] = value
#
# for product in search_products:
#     if product in bakery.keys():
#         quantity = bakery[product]
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")

# Task 3 Statistics

products ={}

while True:
    command = input()
    if command == "statistics":
        break
    items = command.split(": ")
    for index in range(0, len(items), 2):
        key = items[index]
        value = int(items[index + 1])
        if key not in products:
            products[key] = 0
        products[key] += value


print(f"Products is stock:")
for elem in products:
    print(f"- {elem}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
