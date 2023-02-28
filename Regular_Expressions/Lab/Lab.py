# Task 1 Match Full Name
import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
names = input()

valid_names = re.findall(pattern, names)
print("".join(valid_names))

# Task 2 Match Phone Number

import re

phone_numbers = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
valid_numbers = re.findall(pattern, phone_numbers)

print(", ".join(valid_numbers))

# Task 3 Match Dates
import re

pattern = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
dates = input()

matches = re.finditer(pattern, dates)

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")


# Task 4 Match Numbers
import re

text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]*)?($|(?=\s))"

matches = re.finditer(pattern, text)

result = []
for match in matches:
    result.append(match.group())

print(",".join(result))
