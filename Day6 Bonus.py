"""
Prompt:
return a new sorted merged list from K sorted lists, each with size N
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import List, SupportsFloat
import math


def check_min(list_minimum: List[SupportsFloat], list_maximum: List[SupportsFloat], current_minimum: SupportsFloat,
              current_maximum: SupportsFloat, sorted_list: List[SupportsFloat]) -> None:
    """
    Removes the rest of the elements when one of the lists is empty.
    :param list_minimum: the list that the smallest element came from
    :param list_maximum: the list that the larger of the current elements came from
    :param current_minimum: the current smallest element
    :param current_maximum: the larger of the current elements
    :param sorted_list: the output list
    :return: None
    """
    sorted_list.append(current_minimum)
    current: SupportsFloat = (list_minimum or list_maximum).pop(0)
    while list_minimum or list_maximum:
        if current_maximum <= current:
            sorted_list.append(current_maximum)
            sorted_list += list_minimum or list_maximum
        else:
            sorted_list.append(current)
            current = (list_minimum or list_maximum).pop(0)
    if not (list_minimum or list_maximum):
        if current_maximum <= current:
            sorted_list.append(current_maximum)
            sorted_list.append(current)
        else:
            sorted_list.append(current_minimum)
            sorted_list.append(current)


def check_ends(list_one: List[SupportsFloat], list_two: List[SupportsFloat], current_one: SupportsFloat,
               current_two: SupportsFloat, sorted_list: List[SupportsFloat]) -> None:
    """
    Checks to see if one of the lists is empty and empties the other if so.
    :param list_one: the first list to check
    :param list_two: the other list to check
    :param current_one: the current element from the first list
    :param current_two: the current element from the second list
    :param sorted_list: the output list
    :return: None
    """
    if not (list_one and list_two):
        if current_one <= current_two:
            check_min(list_one, list_two, current_one, current_two, sorted_list)
        else:
            check_min(list_two, list_one, current_two, current_one, sorted_list)


def put_min_in(list_minimum: List[SupportsFloat], list_maximum: List[SupportsFloat], minimum: SupportsFloat, maximum:
SupportsFloat, sorted_list: List[SupportsFloat]) -> None:
    """
    Puts in the minimum value and checks if either list is empty.
    :param list_minimum: the list that the current minimum value came from
    :param list_maximum: the list that the larger of the current values came from
    :param minimum: the larger of the current values
    :param maximum: the smaller of the current values
    :param sorted_list: the output list
    :return: None
    """
    sorted_list.append(minimum)
    minimum = list_minimum.pop(0)
    check_ends(list_minimum, list_maximum, minimum, maximum, sorted_list)


def merge(list_one: List[SupportsFloat], list_two: List[SupportsFloat]) -> List[SupportsFloat]:
    """
    Returns a sorted list merged from the two input sorted lists.
    :param list_one: the first sorted list
    :param list_two: the second sorted list
    :return: the sorted merged output
    """
    sorted_list: List[SupportsFloat] = []
    if not (list_one and list_two):
        return list_one or list_two
    current_one: SupportsFloat = list_one.pop(0)
    current_two: SupportsFloat = list_two.pop(0)
    check_ends(list_one, list_two, current_one, current_two, sorted_list)
    while list_one and list_two:
        if current_one <= current_two:
            put_min_in(list_one, list_two, current_one, current_two, sorted_list)
        else:
            put_min_in(list_two, list_one, current_two, current_one, sorted_list)
    return sorted_list


def sort(lists: List[List[SupportsFloat]]) -> List[SupportsFloat]:
    """
    Merges a list of sorted lists into one sorted list.
    :param lists: the list of sorted lists to merge
    :return: the merged sorted list
    """
    while 2 ** math.ceil(math.log2(len(lists))) != len(lists):
        lists.append([])
    for i in range(math.ceil(math.log2(len(lists)))):
        print(lists)
        lists = [merge(*j) for j in zip(*[lists.__iter__()] * 2)]
    return lists[0]


if __name__ == "__main__":
    print(sort([[2, 4, 5], [3, 5, 435], [3, 35, 65], [2, 53, 565]]))
