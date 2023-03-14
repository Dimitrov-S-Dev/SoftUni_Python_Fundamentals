import re
# Task 1 Capture the Numbers
# pattern = r"\d+"
#
# text = input()
# while text:
#     match = re.findall(pattern, text)
#     if match:
#         print(" ".join(match),end=" ")
#     text = input()

# Task 2 Find Variable Names in Sentences

# pattern = r"\b\_[A-Za-z0-9]+\b"
# text = input()
#
# matches = re.findall(pattern, text)
# result = []
# for match in matches:
#     result.append(match[1:])
# print(",".join(result),end="")

# Task 3 Find Occurrences of Word in Sentence

# text = input()
# pattern = input()
#
# match = re.findall(pattern, text, re.IGNORECASE)
# print(len(match))

# Task 4 Extract Email

pattern = r"[a-z0-9\-\_\.\,]+@[A-Za-z-]+[a-z\.]*\b"

text = input()
while text:
    match = re.findall(pattern, text)
    if match:
        print("\n".join(match))
    text = input()

