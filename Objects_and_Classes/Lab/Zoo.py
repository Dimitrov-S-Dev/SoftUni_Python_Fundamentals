"""
Create a class Zoo. It should have a class attribute called __animals that
stores the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo.
There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:
· add_animal(species, name) - based on the species adds the name to the corresponding list
· get_info(species) - based on the species returns a string in the following format:
"{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"
On the first line you will receive the name of the zoo. On the second line you will receive number n.
On the next n lines you will receive animal info in the format: "{species} {name}".
Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish or bird.
On the final line you will receive a species.
At the end, print all the info for that species and the total count of animals.
"""


class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammal in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
