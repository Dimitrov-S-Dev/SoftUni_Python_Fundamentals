text = input()
result = []

for index, value in enumerate(text):
	if value.isupper():
		result.append(index)
print(result)
