"""
Write a program, which reads a string and skips through it,
extracting a hidden message.
The algorithm you should implement is as follows:
Let us take the string "skipTest_String044160"
as an example.
Take every digit from the string and transfer it somewhere.
After this operation, you should have two lists of items
- a numbers list and a non-numbers list:
· Numbers' list: [0, 4, 4, 1, 6, 0]
· Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
After that, take every digit in the numbers list
and split it up into a take list and a skip list.
In the take list, you should keep all digits at an even index.
In the skip list, you should keep all digits at an odd index.
· Numbers' list: [0, 4, 4, 1, 6, 0]
· Take list: [0, 4, 6]
· Skip list: [4, 1, 0]
Afterward, iterate over both lists:
· First, take m characters from the non-numbers list
 and store it in a result string
· Then, skip n characters from the non-numbers list
Note that the skipped characters are summed up as they go.
The process would look like this:
1. Current string: "skipTest_String".
Take 0 characters and skip 4 characters:
· Taken string: ""
· Skipped string: "skip"
2. The remaining string looks like this:
"Test_String". Take 4 characters and skip 1 character:
· Taken string: "Test"
· Skipped string: "_"
3. The string looks like this:
"String". Take 6 characters and skip 0 characters:
· Taken string: "String"
· Skipped string: ""
4. The final string is "TestString".
After that, print the final string on the console.
"""

def get_char(lst):
    return [el for el in lst if not el.isdigit()]


def get_numbers(lst):
    return [int(el) for el in lst if el.isdigit()]


def get_even(lst):
    even = []
    for index, value in enumerate(lst):
        if index % 2 == 0:
            even.append(value)
    return even


def get_odd(lst):
    odd = []
    for index, value in enumerate(lst):
        if index % 2 != 0:
            odd.append(value)
    return odd


def get_result(lst):
    message = ""
    characters = get_char(lst)
    numbers = get_numbers(lst)
    take_list = get_even(numbers)
    skip_list = get_odd(numbers)

    while take_list:
        char_to_take = take_list.pop(0)
        if char_to_take == 0:
            message += ""
            skip = skip_list.pop(0)
            characters = characters[skip:]
        else:
            skip = skip_list.pop(0)
            message += "".join(characters[:char_to_take])
            characters = characters[char_to_take + skip:]
    return message


text = list(input())

print(get_result(text))
