def get_palindrome(num):
    return num == num[:: -1]


numbers_as_str = input().split(', ')
for number in numbers_as_str:
    print(get_palindrome(number))
