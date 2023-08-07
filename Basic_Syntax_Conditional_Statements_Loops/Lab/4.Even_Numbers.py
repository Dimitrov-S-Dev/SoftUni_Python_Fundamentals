n = int(input())

for _ in range(n):
    curr_number = int(input())
    if curr_number % 2 != 0:
        print(f"{curr_number} is odd!")
        break
else:
    print("All numbers are even.")
