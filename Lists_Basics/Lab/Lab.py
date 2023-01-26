# Task 1 Strange Zoo

tail = input()
body = input()
head = input()

result = [head, body, tail]
print(result)

#  Task 2 Courses

count_iter = int(input())
courses = []

for _ in range(count_iter):
    course_name = input()
    courses.append(course_name)
print(courses)

# Task 3 List Statistics

count_iter = int(input())
positive = []
negative = []

for _ in range(count_iter):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")

# Task 4 Search

count_iter = int(input())
search_word = input()
result = []
word_in_result = []

for _ in range(count_iter):
    current_word = input()
    if search_word in current_word:
        word_in_result.append(current_word)
    result.append(current_word)

print(result)
print(word_in_result)

# Task 5 Numbers Filter

count_iter = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
numbers = []

for _ in range(count_iter):
    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []
for num in numbers:
    filtered_pass = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filtered_pass:
        filtered_numbers.append(num)

print(filtered_numbers)
