"""
On the first line, you will receive a sequence of targets
with their integer values, split by a single space.
Then, you will start receiving commands for manipulating
the targets until the "End" command.
The commands are the following:
•	"Shoot {index} {power}"
o	Shoot the target at the index if it exists by reducing
its value by the given power (integer value).
o	Remove the target if it is shot.
A target is considered shot when its value reaches 0.
•	"Add {index} {value}"
o	Insert a target with the received value at the received index
if it exists.
o	If not, print: "Invalid placement!"
•	"Strike {index} {radius}"
o	Remove the target at the given index and the ones
before and after it depending on the radius.
o	If any of the indices in the range is invalid, print:
"Strike missed!" and skip this command.
 Example:  "Strike 2 2"
{radius}	{radius}	{strikeIndex}	{radius}	{radius}
•	"End"
o	Print the sequence with targets in the following format
and end the program:
"{target1}|{target2}…|{target}"
"""


def get_shoot(lst, index, value):
    if 0 <= index < len(lst):
        if lst[index] > value:
            lst[index] -= value
        else:
            lst.pop(index)
    return lst


def get_add(lst, index, value):
    if 0 <= index < len(lst):
        lst.insert(index, value)
    else:
        print(f"Invalid placement!")
    return lst


def get_strike(lst, index, value):
    if index - value >= 0 and index + value < len(lst):
        start = index - value
        end = index + value
        lst = [lst[i] for i in range(len(lst)) if i < start or i > end]
        return lst
    else:
        print(f"Strike missed!")


def get_moving_target(lst):
    while True:
        command = input()
        if command == "End":
            break
        action, index, value = command.split()
        index = int(index)
        value = int(value)

        if action == "Shoot":
            lst = get_shoot(lst, index, value)

        elif action == "Add":
            lst = get_add(lst, index, value)

        elif action == "Strike":
            lst = get_strike(lst, index, value)

    return '|'.join([str(el) for el in lst])


targets = list(map(int, input().split()))
print(get_moving_target(targets))
