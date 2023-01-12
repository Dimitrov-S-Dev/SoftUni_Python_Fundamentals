"""
Using comprehension, write a program that receives
a text and removes all its vowels, case-insensitive.
Print the new text string after removing the vowels.
The vowels that
should be considered are 'a', 'o', 'u', 'e', 'i'.
"""

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [x for x in text if x.lower() not in vowels]
print(''.join(result))
