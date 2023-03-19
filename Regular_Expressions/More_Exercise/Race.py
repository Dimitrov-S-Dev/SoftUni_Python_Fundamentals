# Task 1 Race

# import re
#
# names = input().split(", ")
# names_dict = {}
#
# for name in names:
#     names_dict[name] = 0
#
# while True:
#     distance = 0
#     text = input()
#     if text == "end of race":
#         break
#
#     name_pattern = r"[A-Za-z]"
#     distance_pattern = r"\d"
#     name_match = re.findall(name_pattern, text)
#     p_name = "".join(name_match)
#     distance_match = re.findall(distance_pattern, text)
#     if p_name not in names_dict.keys():
#         continue
#     for digit in distance_match:
#         distance += int(digit)
#     names_dict[p_name] += distance
#
# x = {k: v for k, v in sorted(names_dict.items(), key=lambda item: item[1], reverse=True)}
# count = 0
# for k in x.keys():
#     count += 1
#     if count == 1:
#         print(f"1st place: {k}")
#     elif count == 2:
#         print(f"2nd place: {k}")
#     else:
#         print(f"3rd place: {k}")
#     if count == 3:
#         break

# Task 2