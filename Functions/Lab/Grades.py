def get_grade(num):
    if 2 <= num <= 2.99:
        return 'Fail'
    elif num <= 3.49:
        return 'Poor'
    elif num <= 4.49:
        return 'Good'
    elif num <= 5.49:
        return 'Very Good'
    else:
        return 'Excellent'
    

grade = float(input())
print(get_grade(grade))
