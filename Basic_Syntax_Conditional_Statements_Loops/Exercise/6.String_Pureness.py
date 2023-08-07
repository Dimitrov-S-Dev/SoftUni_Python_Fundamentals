n = int(input())

characters = ",._"
for _ in range(n):
    curr_text = input()
    for char in curr_text:
        if char in characters:
            print(f"{curr_text} is not pure!")
            break
    else:
        print(f"{curr_text} is pure.")
