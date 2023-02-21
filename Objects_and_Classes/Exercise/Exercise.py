# Task 1 Storage

class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")

print(storage.get_products())


# Task 2 Weapon

class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets:
            self.bullets -= 1
            return f"Shooting"
        return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

# Task 3 Catalogue

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

# Task 4 Town

class Town:

    def __init__(self, name:str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

# Task 5 Class

class Class:
    __students_count = 22
    def __init__(self, name:str):
        self.name = name
        self.students = []
        self.grades = []
    def add_student(self, name:str, grade:float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return f"{average_grade:.2f}"

    def __repr__(self):
        return f"The students in {self.name}: {','.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

# Task 6 Inventory

class Inventory:
    
    def __init__(self, capacity:int):
        self.__capacity = capacity
        self.items = []
        
    def add_item(self, item:str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        current_capacity = self.__capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)