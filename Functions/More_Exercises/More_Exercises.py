# Task 1 Data Types

def get_data_type(text, num):
    if text == 'int':
        return num * 2
    elif text == 'real':
        return float(num * 1.5)
    else:
        return f'${num}$'


string_type = input()
number = int(input())
print(get_data_type(string_type, number))

# Task 2 Center point

def get_center_point(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

"""
the Euclidean formula between two points in coord. sys
"""
_x1 = float(input())
_y1 = float(input())
_x2 = float(input())
_y2 = float(input())
dist_x1_y1 = get_center_point(_x1, _y1, 0, 0)
dist_x2_y2 = get_center_point(0, 0, _x2, _y2)
if dist_x1_y1 < dist_x2_y2:
    print(f"({int(_x1)},{int(_y1)})")
else:
    print(f"({int(_x2)},{int(_y2)})")

# Task 3 Longer line

def Rec(n) :
# #Check number and return 1 at zero index positon
#     if(n==0):
#         return 1
# #Check number and return 1 at one index positon
    if (n==1):
        return 1
#Check number and return 1 at second index positon
    elif (n==2):
        return 1
#Check number and return 1 at Third index positon
    elif(n==3):
        return 2
#Check number and return 3 at fourth index positon
    elif(n==4):
        return 4
#If number is greater then 4 then it return sum of previous three numbers
    else:
        return (Rec(n - 1) +
                Rec(n - 2) +
                Rec(n - 3))


#Take the input from user
n = int(input())
#For Loop which used to print the series upto n+1
for i in range(1, n+1):
    print(Rec(i), end=" ")


# Task 5.Mid-Exam-Preparation Multiplication Sign

def get_negative_positive(lst):
    for digit in lst:
        if digit < 0:
            return True
    return False


first_num = int(input())
second_num = int(input())
third_num = int(input())
number_lst = [first_num, second_num, third_num]

if get_negative_positive(number_lst):
    print("negative")
else:
    print("positive")
