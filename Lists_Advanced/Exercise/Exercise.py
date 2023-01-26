# Task 1 Which Are In?

first = input().split(", ")
second = input().split(", ")
result = []

for w1 in first:
    for w2 in second:
        if w1 in w2 and w1 not in result:
            result.append(w1)

print(result)

# Task 2 Next Version


def get_version(lst):
    version_int = int("".join(lst)) + 1
    version_lst = [num for num in str(version_int)]
    print(".".join(version_lst))


version_str = input().split(".")
get_version(version_str)

# Task 3 Word Filter

text = input().split()
result = [el for el in text if len(el) % 2 == 0]

for word in result:
    print(word)




