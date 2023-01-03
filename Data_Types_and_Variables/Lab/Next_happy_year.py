year = int(input())

while True:
    year += 1
    year_to_str = str(year)
    set_year = set(year_to_str)
    if len(year_to_str) != len(set_year):
        continue
    else:
        print(year_to_str)
        break
