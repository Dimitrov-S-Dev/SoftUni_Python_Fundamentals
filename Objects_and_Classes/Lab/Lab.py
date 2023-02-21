# Task 1 Comment

class Comment:

    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

# Task 2 Party

class Party:

    def __init__(self):
        self.people = []

persons = Party()

while True:
    name = input()
    if name == "End":
        break
    persons.people.append(name)

print(f"Going: ', '.join{persons.people}")
print(f"Total: {len(persons.people)}")


