# Task 1 Count Chars in a String

# words_list = input().split()
# word = "".join(words_list)
# result = {}
#
# for char in word:
#     if char not in result.keys():
#         result[char] = 0
#     result[char] += 1
#
# for key, value in result.items():
#     print(f"{key} -> {value}")

# Task 2 A Miner Task

# result = {}
#
# while True:
#     element = input()
#     if element == "stop":
#         break
#     value = int(input())
#     if element not in result.keys():
#         result[element] = 0
#     result[element] += value
#
#
# for key, value in result.items():
#     print(f"{key} -> {value}")

# Task 3 Capitals

countries = input().split(", ")
capitals = input().split(", ")

result = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in result.items():
    print(f"{key} -> {value}")
