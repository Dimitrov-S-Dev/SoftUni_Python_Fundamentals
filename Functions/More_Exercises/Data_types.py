def get_data_type(text, num):
    if text == 'int':
        return int(num)
    elif text == 'real':
        return float(num)
    else:
        return f'${num}$'


string_type = input()
number = input()
print(get_data_type(string_type, number))