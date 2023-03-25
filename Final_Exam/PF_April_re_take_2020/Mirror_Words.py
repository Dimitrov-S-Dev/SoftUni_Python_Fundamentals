import re

pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
text = input()

matches = re.findall(pattern, text)
result = []
if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match[1] == match[2][::-1]:
            result.append(f"{match[1]} <=> {match[2]}")

else:
    print(f"No word pairs found!")

if result:
    print(f"The mirror words are:")
    print(", ".join(result))
else:
    print(f"No mirror words!")
