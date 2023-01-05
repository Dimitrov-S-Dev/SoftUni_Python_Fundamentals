words = input().split()
searched_word = input()

palindromes = [x for x in words if x == x[:: -1]]
count = palindromes.count(searched_word)

print(palindromes)
print(f"Found palindrome {count} times")
