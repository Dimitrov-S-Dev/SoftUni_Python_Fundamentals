"""
On the first line, you will receive words separated by a single space.
On the second line,you will receive a palindrome.
First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format:
"Found palindrome {number} times".
"""

words = input().split()
searched_word = input()

palindromes = [x for x in words if x == x[:: -1]]
count = palindromes.count(searched_word)

print(palindromes)
print(f"Found palindrome {count} times")
