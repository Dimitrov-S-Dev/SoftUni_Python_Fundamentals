import re

emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
numbers_pattern = r"(\d)"
text = input()

threshold = 1
e_matches = re.findall(emoji_pattern, text)
n_matches = re.findall(numbers_pattern, text)

for num in n_matches:
    threshold *= int(num)
cool_emoji = []
for elem in e_matches:
    cur_sum = 0
    for char in elem[1]:
        cur_sum += ord(char)
    if cur_sum > threshold:
        cool_emoji.append(elem)
print(f"Cool threshold: {threshold}")
print(f"{len(e_matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emoji:
    print(''.join(emoji), end=" \n")
