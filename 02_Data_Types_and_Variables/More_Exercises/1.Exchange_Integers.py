first = int(input())
second = int(input())
print(f'Before:\na = {first}\nb = {second}')
first, second = second, first
print(f'After:\na = {first}\nb = {second}')
