age = int(input())

result = f"drink "

if age <= 14:
    result += "toddy"
elif age <= 18:
    result += "coke"
elif age <= 21:
    result += "beer"
else:
    result += "whisky"

print(result)
