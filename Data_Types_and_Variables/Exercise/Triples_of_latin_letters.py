count_iter = int(input())

for i in range(count_iter):
    for j in range(count_iter):
        for k in range(count_iter):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
