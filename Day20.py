"""
Prompt:
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of
rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from typing import Tuple, List
from collections import defaultdict

__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#  4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


def min_classrooms(timetable: List[Tuple[int, int]]) -> int:
    """
    Returns the minimum number of classrooms that are needed for the timetable of start and end points
    :param timetable:
    :return:
    """
    rooms = defaultdict(lambda: 0)
    for i in timetable:
        for j in range(i[0], i[1]):
            rooms[j] += 1
    return max(rooms.values())


if __name__ == "__main__":
    print(f"{min_classrooms([(30, 75), (0, 50), (60, 150)]) = }")
