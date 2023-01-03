count_iter = int(input())

for a in range(count_iter):
    for b in range(count_iter):
        for c in range(count_iter):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")
