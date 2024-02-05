number_list = list(map(int, input()))
number_list.sort(reverse=True)
print(*number_list, sep="")
