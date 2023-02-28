# Task 1 Match Full Name
# import re
#
# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
# names = input()
#
# valid_names = re.findall(pattern, names)
# print("".join(valid_names))

# Task 2 Match Phone Number

# import re
#
# phone_numbers = input()
# pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
# valid_numbers = re.findall(pattern, phone_numbers)
#
# print(", ".join(valid_numbers))

# Task 3 Match Dates
import re

pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})(\2)([0-9]{4})"
dates = input()

result = re.findall(pattern, dates)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[4]}")




