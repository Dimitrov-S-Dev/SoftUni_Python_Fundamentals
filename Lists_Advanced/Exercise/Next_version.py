def get_version(lst):
    version_int = int("".join(lst)) + 1
    version_lst = [num for num in str(version_int)]
    print(".".join(version_lst))


version_str = input().split(".")
get_version(version_str)
