number_of_lines = int(input())
is_balanced = True
is_open = False

for _ in range(number_of_lines):
    char = input()
    if char == "(":
        if is_open:
            is_balanced = False
        else:
            is_open = True
    elif char == ")":
        if is_open:
            is_open = False
        else:
            is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
