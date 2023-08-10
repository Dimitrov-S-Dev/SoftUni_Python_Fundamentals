year = int(input())

while True:
    year += 1
    year_to_str = str(year)
    year_set = set(year_to_str)
    if len(year_to_str) == len(year_set):
        print(year_to_str)
        break
