number = float(input())

result = ""
if number == 0:
    result = "zero"
elif number > 0:
    if number > 1_000_000:
        result = "large positive"
    elif number < 1:
        result = "small positive"
    else:
        result = "positive"
else:
    if abs(number) > 1_000_000:
        result = "large negative"
    elif abs(number) < 1:
        result = "small negative"
    else:
        result = "negative"

print(result)
