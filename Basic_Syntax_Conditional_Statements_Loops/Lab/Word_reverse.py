"""
Write a program that receives a single word,
reverses it, and prints it.
"""

word = input()
# reversed_word = ""
# for index in range(len(word) - 1, -1, -1):
# 	reversed_word += word[index]
# print(reversed_word)
reversed_word = word[::-1]
print(reversed_word)
