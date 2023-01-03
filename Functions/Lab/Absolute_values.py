# def abs_num(lst):
#     result = []
#     for num in lst:
#         result.append(abs(num))
#     return result
#
# numbers = list(map(float,input().split()))
# print(abs_num(numbers))

numbers = list(map(float, input().split()))
result = [abs(num) for num in numbers]
print(result)