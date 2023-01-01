key = int(input())
count_iter = int(input())
message = ""

for _ in range(count_iter):
    current_letter = (input())
    ascid_num = ord(current_letter) + key
    message += chr(ascid_num)

print(message)
