number_of_coffees = 0

while True:
    command = input()

    if command == "END":
        break

    if command.lower() in ["coding", "dog", "cat", "movie"]:
        if command.islower():
            number_of_coffees += 1
        else:
            number_of_coffees += 2

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)
