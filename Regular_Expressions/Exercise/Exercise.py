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

pattern = r"\b\_[A-Za-z0-9]+\b"
text = input()

matches = re.findall(pattern, text)
result = []
for match in matches:
    result.append(match[1:])
print(",".join(result),end="")

