import re
# Task 1 Capture the Numbers
pattern = r"\d+"

text = input()
while text:
    match = re.findall(pattern, text)
    if match:
        print(" ".join(match),end=" ")
    text = input()

