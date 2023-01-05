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
