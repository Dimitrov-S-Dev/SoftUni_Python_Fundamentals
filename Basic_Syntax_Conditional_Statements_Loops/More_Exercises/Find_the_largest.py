number = list(map(int, input()))
number.sort(reverse=True)
print(*number, sep="")
