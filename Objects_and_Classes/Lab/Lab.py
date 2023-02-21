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

# Task 3 Email

class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())



