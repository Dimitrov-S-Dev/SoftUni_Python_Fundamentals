# Task 1 Activation Keys

def get_contains(text, sub_text):
    if sub_text in text:
        print(f"{text} contains {sub_text}")
    else:
        print(f"Substring not found!")


def get_flip(text, command, start, end):
    if command == "Upper":
        text = text[0:start] + text[start:end].upper() + text[end:]

    elif command == "Lower":
        text = text[0:start] + text[start:end].lower() + text[end:]
    print(text)
    return text

def get_slice(text, start, end):
    text = text[0:start] + text[end:]
    print(text)
    return text
def get_while(text):
    while True:
        command = input()
        if command == "Generate":
            break
        info = command.split(">>>")
        action = info[0]

        if action == "Contains":
            substring = info[1]
            get_contains(text, substring)
        elif action == "Flip":
            upper_lower = info[1]
            start_index = int(info[2])
            end_index = int(info[3])
            text = get_flip(text,upper_lower, start_index, end_index)
        elif action == "Slice":
            start_index = int(info[1])
            end_index = int(info[2])
            text = get_slice(text, start_index, end_index)
    print(f"Your activation key is: {text}")

def get_activation_keys(text):
    text = get_while(text)

data = input()
get_activation_keys(data)

# Task 2

import re
n = int(input())
for _ in range(n):
    curr_barcode = input()
    pattern = r"(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])"
    match = re.search(pattern, curr_barcode)
    if match:
       num = r"\d"
       numbers = re.findall(num, match.group())
       if numbers:
           print(f"Product group: {''.join(numbers)}")
       else:
           print(f"Product group: 00")
    else:
        print(f"Invalid barcode")

# Task 3 Need for Speed III

def get_info(number):
    car_dict = {}
    for _ in range(number):
        car, mileage, fuel = input().split("|")
        mileage = int(mileage)
        fuel = int(fuel)
        car_dict[car] = {"mileage": mileage, "fuel": fuel}

    return car_dict

def get_while(dict):
    while True:
        command = input()
        if command == "Stop":
            break
        info = command.split(" : ")
        action = info[0]
        car = info[1]
        if action == "Drive":
            distance = int(info[2])
            fuel = int(info[3])
            if dict[car]["fuel"] >= fuel:
                dict[car]["mileage"] += distance
                dict[car]["fuel"] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if dict[car]["mileage"] >= 100_000:
                    print(f"Time to sell the {car}!")
                    del dict[car]
            else:
                print(f"Not enough fuel to make that ride")

        elif action == "Refuel":
            fuel = int(info[2])
            curr_fuel = dict[car]["fuel"]
            if curr_fuel + fuel > 75:
                dict[car]["fuel"] = 75
            else:
                dict[car]["fuel"] += fuel
            diff = dict[car]["fuel"] - curr_fuel
            print(f"{car} refueled with {diff} liters")

        elif action == "Revert":
            kilometers = int(info[2])
            dict[car]["mileage"] -= kilometers
            if dict[car]["mileage"] < 10_000:
                dict[car]["mileage"] = 10_000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")
    return dict

def get_print(dict):
    for car in dict.keys():
        print(f"{car} -> Mileage: {dict[car]['mileage']} kms, Fuel in the tank: {dict[car]['fuel']} lt.")
def get_need_for_speed(num):
    cars_dict = get_info(n)
    cars_dict = get_while(cars_dict)
    cars_dict = get_print(cars_dict)


n = int(input())
get_need_for_speed(n)
