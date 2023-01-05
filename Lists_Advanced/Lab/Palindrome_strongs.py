words = input().split()
palindrome = input()

palindromes = [x for x in words if x == x[:: -1]]
count = palindromes.count(palindrome)

print(palindromes)
print(f"Found palindrome {count} times")
