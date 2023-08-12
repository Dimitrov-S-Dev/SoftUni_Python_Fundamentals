key = int(input())
n = int(input())
message = ''

for _ in range(n):
    current_char_num = ord(input())
    current_char_num += key
    message += chr(current_char_num)

print(message)
