text = input().lower()
words = ['sand', 'water', 'fish', 'sun']
count = 0

for word in words:
    count += text.count(word)

print(count)
