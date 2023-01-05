import math


def get_center_point(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

"""
the Euclidean formula between two points in coord. sys
"""
_x1 = float(input())
_y1 = float(input())
_x2 = float(input())
_y2 = float(input())
dist_x1_y1 = get_center_point(_x1, _y1, 0, 0)
dist_x2_y2 = get_center_point(0, 0,_x2, _y2)
if dist_x1_y1 < dist_x2_y2:
    print(f"({int(_x1)},{int(_y1)})")
else:
    print(f"({int(_x2)},{int(_y2)})")
