n = int(input())
brackets = []

for _ in range(n):
    curr_element = input()
    if curr_element == '(':
        if "(" in brackets:
            print('UNBALANCED')
            break
        brackets.append(curr_element)
    elif curr_element == ')':
        if '(' not in brackets:
            print('UNBALANCED')
            break
        brackets.remove('(')
else:
    print('BALANCED')
