# messages = input().split()
# final_message = []
#
# for message in messages:
#     number = ""
#     current_message = ""
#     for character in message:
#         if character.isdigit():
#             number += character
#         else:
#             break
#     message = message.replace(number, "")
#     number = int(number)
#     current_message += chr(number)
#     if len(message) > 1:
#         message = message[-1] + message[1: - 1] + message[0]
#     current_message += message
#     final_message.append(current_message)
#
# print(" ".join(final_message))

messages = input().split()
decipher_message = []

for message in messages:
    char = [el for el in message if not el.isdigit()]
    digit = [el for el in message if el.isdigit()]
    char_digit = [chr(int("".join(digit)))]
    char[0], char[-1] = char[-1], char[0]
    new_message = char_digit + char
    decipher_message.append("".join(new_message))

print(" ".join(decipher_message))
