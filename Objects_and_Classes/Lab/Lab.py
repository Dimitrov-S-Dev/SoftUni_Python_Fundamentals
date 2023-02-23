# Task 1 Comment

class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

# Task 2 Party

class Party:

    def __init__(self):
        self.people = []

persons = Party()

while True:
    name = input()
    if name == "End":
        break
    persons.people.append(name)

print(f"Going: ', '.join{persons.people}")
print(f"Total: {len(persons.people)}")

# Task 3 Email

class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())

# Task 4 Zoo

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammals":
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
counter = int(input())

for i in range(counter):
    species, name = input().split()
    if species == "mammals":
        zoo.add_animal(species, name)
    elif species == "fishes":
        zoo.add_animal(species, name)
    elif species == "birds":
        zoo.add_animal(species, name)

species_name = input()
print(zoo.get_info(species_name))

# Task 5 Circle

class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius ** 2

    def calculate_area_of_sector(self, sector_angle):
        return (sector_angle / 360) * Circle.__pi * self.radius ** 2


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
