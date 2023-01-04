def get_loading_bar(num):
    if num == 100:
        return f"100% Complete!\n [%%%%%%%%%%]"
    return f"{num}% [{'%' * (num//10)}{'.' * (10 - num// 10)}]\n Still loading..."


number = int(input())
print(get_loading_bar(number))
