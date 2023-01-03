def get_round(lst):
    rounds = []
    for num in lst:
        rounds.append(int(num))
    return rounds

numbers = list(map(float, input().split()))
print(get_round(numbers))
