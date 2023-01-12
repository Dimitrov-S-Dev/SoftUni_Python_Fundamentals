"""
Using comprehension, write a program that receives some text,
separated by space, and take only those words whose length is even.
Print each word on a new line.
"""

text = input().split()
result = [el for el in text if len(el) % 2 == 0]

for word in result:
    print(word)
