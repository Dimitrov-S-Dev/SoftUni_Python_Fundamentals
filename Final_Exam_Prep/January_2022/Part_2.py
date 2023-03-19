# Task 1 World Tour

# def get_while(string):
#     while True:
#         command = input()
#         if command == "Travel":
#             break
#         info = command.split(":")
#         action = info[0]
#
#         if action == "Add Stop":
#             index = int(info[1])
#             str = info[2]
#             if index in range(len(string)):
#                 string = string[0:index] + str + string[index:]
#             print(string)
#         elif action == "Remove Stop":
#             start_index = int(info[1])
#             end_index = int(info[2])
#             if start_index in range(len(string)) and end_index in range(len(string)):
#                 end_index += 1
#                 string = string[0: start_index] + string[end_index:]
#             print(string)
#
#         elif action == "Switch":
#             old = info[1]
#             new = info[2]
#             if old in string:
#                 string = string.replace(old, new)
#             print(string)
#
#     return string
#
#
# def get_print(string):
#     print(f"Ready for world tour! Planned stops: {string}")
# def get_world_tour(string):
#     string = get_while(string)
#     get_print(string)
#
#
# text = input()
# get_world_tour(text)