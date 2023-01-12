"""
On the first input line, you will receive the initial schedule
of lessons and exercises that will be part of the next course,
separated by a comma and a space ", ".
Until you receive the "course start" command,
you will be given some commands to modify the course schedule.
The possible commands are:

· "Add:{lessonTitle}" - add the lesson to the end of the schedule
if it does not exist.
· "Insert:{lessonTitle}:{index}" - insert the lesson
to the given index, if it does not exist.
· "Remove:{lessonTitle}" - remove the lesson, if it exists.
· "Swap:{lessonTitle}:{lessonTitle}" - swap the position
of the two lessons if they exist.
· "Exercise:{lessonTitle}" - add Exercise in the schedule
right after the lesson index,
if the lesson exists and there is no exercise already,
in the following format "{lessonTitle}-Exercise".
If the lesson doesn't exist, add the lesson at the end
of the course schedule, followed by the Exercise.
Note: Each time you Swap or Remove a lesson,
you should do the same with the Exercises,
if there are any following the lessons.
"""


def get_add(lst, title):
    if title not in lst:
        lst.append(title)
    return lst


def get_insert(lst, title, index):
    if title not in lst:
        lst.insert(index, title)
    return lst


def get_remove(lst, title):
    if title in lst:
        title_index = lst.index(title)
        if title_index + 1 in range(len(lst)):
            if "Exercise" in lst[title_index + 1]:
                lst.pop(title_index + 1)
        lst.remove(title)
    return lst


def get_swap(lst, title, new_title):
    if title in lst and new_title in lst:
        title_index = lst.index(title)
        new_title_index = lst.index(new_title)
        title_has_exercise = False
        new_has_exercise = False
        if title_index + 1 in range(len(lst)):
            title_has_exercise = "Exercise" in lst[title_index + 1]
        if new_title_index + 1 in range(len(lst)):
            new_has_exercise = "Exercise" in lst[new_title_index + 1]
        lst[title_index], lst[new_title_index] = lst[new_title_index], lst[title_index]
        if title_has_exercise and new_has_exercise:
            lst[title_index + 1], lst[new_title_index + 1] = lst[new_title_index + 1], lst[title_index + 1]
        elif not title_has_exercise and new_has_exercise:
            lst.insert(title_index + 1, lst.pop(new_title_index + 1))
        elif title_has_exercise and not new_has_exercise:
            lst.insert(new_title_index + 1, lst.pop(title_index + 1))
    return lst


def get_exercise(lst, title):
    if title in lst and f"{title}-Exercise" not in lst:
        title_index = lst.index(title)
        lst.insert(title_index + 1, f"{title}-Exercise")
    elif title not in lst:
        lst.append(title)
        lst.append(f"{title}-Exercise")
    return lst


def get_info(lst):
    for index, el in enumerate(lst, 1):
        print(f"{index}.{el}")


def get_data(lst):
    while True:
        command = input().split(":")
        current_command = command[0]
        if current_command == "course start":
            return get_info(lst)
        else:
            title = command[1]
            if current_command == "Add":
                lst = get_add(lst, title)
            elif current_command == "Insert":
                index = int(command[2])
                lst = get_insert(lst, title, index)
            elif current_command == "Remove":
                lst = get_remove(lst, title)
            elif current_command == "Swap":
                new_title = command[2]
                lst = get_swap(lst, title, new_title)
            elif current_command == "Exercise":
                lst = get_exercise(lst, title)


info = input().split(", ")
get_data(info)
