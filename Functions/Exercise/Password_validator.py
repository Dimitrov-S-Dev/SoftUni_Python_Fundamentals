def get_password_valid(word):
    is_valid = []
    if len(word) < 6 or len(word) > 10:
        is_valid.append('Password must be between 6 and 10 characters')
    if not word.isalnum():
        is_valid.append('Password should have only letters and digits')
    count = 0
    for elem in word:
        if elem.isdigit():
            count += 1
    if count < 2:
        is_valid.append('Password must have at least 2 digits')
    return is_valid


password = input()
password_validation = get_password_valid(password)
if len(password_validation) > 0:
    print('\n'.join(password_validation))
else:
    print('Password is valid')


