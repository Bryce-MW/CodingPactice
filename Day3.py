"""
Prompt:
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers
as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


# No bonus question today so only one function

from typing import List


def missing(lower_list: List[int]) -> int:
    """
    Returns the lowest positive integer not in the list.
    :param lower_list: the list to search int
    :return: the lowest positive integer not in the list
    """
    [lower_list.remove(current) for current in lower_list if current <= 0]
    while bool(len([lower_list.remove(current) for current in lower_list if current <= len(lower_list)])):
        pass
    return len(lower_list)
