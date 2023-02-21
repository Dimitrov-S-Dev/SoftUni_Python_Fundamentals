# # Task 1 Storage
#
# class Storage:
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product: str):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#     def get_products(self):
#         return self.storage
#
# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
#
# print(storage.get_products())
#
#
# # Task 2 Weapon
#
# class Weapon:
#
#     def __init__(self, bullets: int):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets:
#             self.bullets -= 1
#             return f"Shooting"
#         return f"no bullets left"
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"
#
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
#
# # Task 3 Catalogue

class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter:str):
        return [el for el in self.products if el.startswith(first_letter)]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue: \n"
        result += '\n'.join(self.products)
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


