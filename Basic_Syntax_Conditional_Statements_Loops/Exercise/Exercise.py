# Task 1 Jenny's Secret Message

name = input()
if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")

# Task 2 Drink Something

age = int(input())
drink_type = ""

if age <= 14:
    drink_type = "toddy"
elif age <= 18:
    drink_type = "coke"
elif age <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"

print(f"drink {drink_type}")

# Task 3 Chat Codes

count_iter = int(input())

for messages in range(count_iter):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message < 88:
        print("GREAT!")
    else:
        print("Bye.")

# Task 4 Maximum Multiple

divisor = int(input())
boundary = int(input())

for num in range(boundary, divisor, -1):
    if num % divisor == 0:
        print(num)
        break

# Task 5.Mid-Exam-Preparation Orders

orders_count = int(input())
total_price = 0

for order in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if 1 <= capsule_per_day <= 2000 and 1 <= days <= 31 and 0.01 <= price_per_capsule <= 100.00:
        price = price_per_capsule * days * capsule_per_day
        print(f"The price for the coffee is: ${price:.2f}")
        total_price += price

print(f"Total: ${total_price:.2f}")

# Task 6 String Pureness

count_iter = int(input())

for word in range(count_iter):
    current_word = input()
    if "," in current_word or "." in current_word or "_" in current_word:
        print(f"{current_word} is not pure!")
    else:
        print(f"{current_word} is pure.")

# Task 7 Double Char

while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    result = ""
    for char in command:
        result += char * 2
    print(result)

# Task 8 ow Much Coffee Do You Need?

command = input()
coffee_count = 0

while command != "END":
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    command = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

# Task 9 Sorting Hat

name = input()
is_break = False

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_break = True
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if not is_break:
    print("Welcome to Hogwarts.")

# Task 10 Mutate Strings

first_word = input()
second_word = input()
final_word = first_word

for index in range(len(first_word)):
    left_part = second_word[: index + 1]
    right_part = first_word[index + 1:]
    current_word = left_part + right_part
    if current_word == final_word:
        continue
    print(current_word)
    final_word = current_word

# ------------>      alternative option      <------------------
# for i in range(len(first_word)):
# 	if first_word[i] != second_word[i]
# 		replacement = second_word[i]
# 		word = first_word[0:i] + replacement + second_word[i +1:]
# 		first_word = word
# 		print(word)

# Task 11 Easter Bread

budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = flour_price * 1.25
bread_price = flour_price + eggs_price + (milk_price / 4)
bread_count = 0
colored_eggs = 0

while budget >= bread_price:
    bread_count += 1
    budget -= bread_price
    colored_eggs += 3
    if bread_count % 3 == 0:
        if colored_eggs > bread_count - 2:
            colored_eggs -= bread_count - 2
        else:
            break

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

# Task 12 Christmas Spirit

decoration_quantity = int(input())
days_to_christmas = int(input())
ornament_price, ornament_points = 2, 5
skirt_price, skirt_points = 5, 3
garland_price, garland_points = 3, 10
lights_price, lights_points = 15, 17
spirit = 0
money = 0

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        decoration_quantity += 2
    if day % 10 == 0:
        spirit -= 20
        money += skirt_price + garland_price + lights_price
    if day % 5 == 0:
        money += lights_price * decoration_quantity
        spirit += lights_points
        if day % 3 == 0:
            spirit += 30
    if day % 3 == 0:
        money += (skirt_price + garland_price) * decoration_quantity
        spirit += skirt_points + garland_points
    if day % 2 == 0:
        money += ornament_price * decoration_quantity
        spirit += ornament_points

if days_to_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
