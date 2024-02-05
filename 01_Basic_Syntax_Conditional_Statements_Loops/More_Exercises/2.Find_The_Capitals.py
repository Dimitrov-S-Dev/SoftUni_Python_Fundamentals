text = input()
result = [x for x in range(len(text)) if text[x].isupper()]
print(result)
