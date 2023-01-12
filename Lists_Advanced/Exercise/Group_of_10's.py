"""
Write a program that receives a sequence of numbers
(a string containing integers separated by ", ")
and prints the numbers sorted into lists of 10's in the format
"Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
"""

lst = list(map(int, input().split(", ")))
gr_10 = [num for num in lst if 0 <= num <= 10]
gr_20 = [num for num in lst if 11 <= num <= 20]
gr_30 = [num for num in lst if 21 <= num <= 30]
gr_40 = [num for num in lst if 31 <= num <= 40]
gr_50 = [num for num in lst if 41 <= num <= 50]

print(f"Group of 10's: {gr_10}")
print(f"Group of 20's: {gr_20}")
print(f"Group of 30's: {gr_30}")
print(f"Group of 40's: {gr_40}")
print(f"Group of 50's: {gr_50}")
