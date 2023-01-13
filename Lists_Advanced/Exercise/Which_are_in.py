"""
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line
"""

first = input().split(", ")
second = input().split(", ")
result = []

for w1 in first:
    for w2 in second:
        if w1 in w2 and w1 not in result:
            result.append(w1)

print(result)